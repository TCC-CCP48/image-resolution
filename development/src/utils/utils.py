# coding: utf-8
#
#   utils.py
#   Objetivo:       Módulo que aloca diversas funções utilizadas em toda a aplicação.
#   Autores:        Caroline, Daniel, Leonardo e Paloma
#   Contato:        tcc.ccp48@gmail.com
#   Data:           15/09/2021

# Imports necessários
import os
import logging
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton
from logging import Logger, FileHandler, Formatter


def botaoComIcone(btn: QPushButton, caminho: str, tamanho: tuple) -> QPushButton:
    """
    Método que configura um ícone para um botão, a partir de uma imagem e tamanho requisitados.
    :param btn: QPushButton a ser configurado.
    :param caminho: str que representa o caminho da imagem a ser adicionada ao botão.
    :param tamanho: tuple com as coordernadas (largura, altura), a serem atribuídas ao QPixmap do ícone.
    :return: QPushButton pronto com ícone configurado, no tamanho requisitado.
    """
    largura, altura = tamanho
    icone = QIcon()
    icone.addPixmap(
            QPixmap(caminho),
            QIcon.Normal,
            QIcon.Off
    )
    btn.setIcon(icone)
    btn.setIconSize(QSize(largura, altura))
    return btn


def configuraLog(nome: str) -> Logger:
    """
    Método que configura log para aquela classe/módulo escolhido, utilizando o mesmo arquivo de log passado.
    :param nome: str que representa o nome que será atribuído àquele log em específico.
    :return: objeto de tipo Logger configurado para alocar as informações do projeto.
    """
    
    arquivoLog: str = os.path.join(os.getcwd(), "..", "other", "log.log")

    # Criando o log
    log: Logger = logging.getLogger(nome)
    log.setLevel(logging.INFO)

    # Atribuindo o FileHandler (para salvar as infos de log no arquivo .log)
    manipuladorArquivo = FileHandler(
            filename=arquivoLog,
            mode='a',
            encoding='UTF-8'
    )

    # Criando o formatador, para espaçar data, nome, nível e mensagem
    formatador = Formatter(
            fmt='%(asctime)-25s %(name)-12s %(levelname)-8s %(msg)s'
    )

    # Compilando o log
    manipuladorArquivo.setFormatter(formatador)
    log.addHandler(manipuladorArquivo)
    
    return log


def nomeDoArquivo(caminho: str) -> str:
    """
    Método para coletar o nome do arquivo, desconsiderando seu caminho total.
    :param caminho: str que representa o caminho total do arquivo.
    :return: str, nome do arquivo.
    """
    # Divivindo o caminho por barra. Resulta numa lista de strings
    divisaoStr: list = caminho.split("/")

    # Coletando o último elemento, isto é, o nome do arquivo. Ex: "arquivo.jpg"
    ultimoElemento: int = len(divisaoStr) - 1
    arquivo: str = divisaoStr[ultimoElemento]

    return arquivo


def constroi_modelo(fatorUpscale=15, canais=1):
    conv_args = {
        "activation": "relu",
        "kernel_initializer": "Orthogonal",
        "padding": "same",
    }
    inputs = keras.Input(shape=(None, None, canais))
    x = layers.Conv2D(64, 5, **conv_args)(inputs)
    x = layers.Conv2D(64, 3, **conv_args)(x)
    x = layers.Conv2D(32, 3, **conv_args)(x)
    x = layers.Conv2D(canais * (fatorUpscale ** 2), 3, **conv_args)(x)
    outputs = tf.nn.depth_to_space(x, fatorUpscale)
    
    model = keras.Model(inputs, outputs)
    
    loss_fn = keras.losses.MeanSquaredError()
    optimizer = keras.optimizers.Adam(learning_rate=0.001)
    model.compile(
        optimizer=optimizer, loss=loss_fn,
    )
    return model


def conversor_alta_resolucao(modelo, img):
    ycbcr = img.convert("YCbCr")
    img_cinza, canal_cb, canal_cr = ycbcr.split()
    img_cinza = img_to_array(img_cinza)
    img_cinza = img_cinza.astype("float32") / 255.0

    entrada = np.expand_dims(img_cinza, axis=0)
    saida = modelo.predict(entrada)

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
    return img_resultado

