# coding: utf-8
#
#   utilsNeuralNetwork.py
#   Objetivo:       Módulo que aloca funções utilizadas para construção e uso do modelo de rede neural.
#   Autores:        Caroline, Daniel, Leonardo e Paloma
#   Contato:        tcc.ccp48@gmail.com
#   Data:           15/09/2021


# Imports necessários
import os
import PIL
import PIL.Image
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import img_to_array


def constroi_modelo(fatorUpscale=8, canais=1) -> object:
    """
    Método para construir o modelo de rede neural correspondente ao ESPCN.
    :param fatorUpscale: inteiro que corresponde à quantidade de vezes que a imagem será aumentada.
    :param canais: inteiro que representa a quantidade de canais de cores utilizadas na construção do modelo.
    :return: modelo (keras.Model) construído com todos os parâmetros escolhidos.
    """

    # Argumentos para a construção de convolução
    conv_args = {
        "activation": "relu",
        "kernel_initializer": "Orthogonal",
        "padding": "same",
    }
    caminhoPesos: str = os.path.join(os.getcwd(), "other", "checkpoint8x", "meu-checkpoint")

    # Construção da sequência das camadas com a utilização dos filtros
    camadaEntrada = keras.Input(shape=(None, None, canais))
    camadaSeguinte = layers.Conv2D(64, 5, **conv_args)(camadaEntrada)
    camadaSeguinte = layers.Conv2D(64, 3, **conv_args)(camadaSeguinte)
    camadaSeguinte = layers.Conv2D(32, 3, **conv_args)(camadaSeguinte)
    camadaSeguinte = layers.Conv2D(canais * (fatorUpscale ** 2), 3, **conv_args)(camadaSeguinte)
    camadaSaida = tf.nn.depth_to_space(camadaSeguinte, fatorUpscale)
    
    # Construção do modelo
    modelo = keras.Model(camadaEntrada, camadaSaida)
    
    # Parametrização de função de perda e otimizador
    loss_fn = keras.losses.MeanSquaredError()
    optimizer = keras.optimizers.Adam(learning_rate=0.001)
    modelo.compile(
        optimizer=optimizer, loss=loss_fn,
    )

    # Carregando os pesos calculados pelo treino prévio
    modelo.load_weights(caminhoPesos)
    return modelo


def conversor_alta_resolucao(modelo: object, img: PIL.Image.Image, fator=8) -> PIL.Image.Image:
    """
    Função que recebe uma imagem e a redimensiona via modelo da rede ESPCN.
    :param modelo: keras.Model a ser utilizado
    :param img: imagem de tipo PIL.Image.Image a ser transformada
    :return: img redimensionada.
    """

    # Convertendo os canais de cor de img para YCbCr     
    ycbcr = img.convert("YCbCr")
    
    # Coletando apenas a representação em cinza (canal Y de YCbCr) e processando o mesmo para ser aceito na rede neural
    img_cinza, canal_cb, canal_cr = ycbcr.split()
    img_cinza = img_to_array(img_cinza)
    img_cinza = img_cinza.astype("float32") / 255.0
    entrada = np.expand_dims(img_cinza, axis=0)

    # Construindo a imagem redimensionada
    saida = modelo.predict(entrada)

    # Reconstruindo a imagem com o canal cinza redimensionado
    saida_img_cinza = saida[0]
    saida_img_cinza *= 255.0
    saida_img_cinza = saida_img_cinza.clip(0, 255)
    saida_img_cinza = saida_img_cinza.reshape(
        (np.shape(saida_img_cinza)[0], 
         np.shape(saida_img_cinza)[1])
    )
    saida_img_cinza = PIL.Image.fromarray(np.uint8(saida_img_cinza), mode="L")
    saida_canal_cb = canal_cb.resize(saida_img_cinza.size, PIL.Image.BICUBIC)
    saida_canal_cr = canal_cr.resize(saida_img_cinza.size, PIL.Image.BICUBIC)
    img_resultado = PIL.Image.merge("YCbCr", 
            (saida_img_cinza, saida_canal_cb, saida_canal_cr)).convert(
        "RGB"
    )
    
    # Redimensionando imagem (se necessário):
    # Se fator for 8, então não será necessário o redimensionamento
    # Se fator for 4, então o redimensionamento será com 2
    # Se fator for 2, então o redimensionamento será com 4
    dictRedimensionamento: dict = {
        2: 4,
        4: 2,
    }

    fatorRedimensionamento = dictRedimensionamento.get(fator, None)
    if fatorRedimensionamento:
        img_resultado = redimensionaImagem(img_resultado, fatorRedimensionamento)

    return img_resultado


def redimensionaImagem(img: PIL.Image.Image, fator: int) -> PIL.Image.Image:
    """
    Função para redimensionar a imagem conforme o fator passado.
    :param img: PIL.Image.Image que será redimensionada
    :param fator: inteiro que será o divisor para o redimensionamento.
    :return: PIL.Image.Image
    """
    return img.resize(
        (img.size[0] // fator, img.size[1] // fator),
        PIL.Image.BICUBIC,
    )

