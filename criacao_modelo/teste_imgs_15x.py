# teste_imgs_15x.py
#
#   Objetivo:   A partir de uma pasta com imagens 'lr' e 'hr', processar as 'lr' com a rede neural x15 e as 'hr' renomear para 'hr_15x'.
#   Autor:      Caroline, Daniel, Leonardo e Paloma
#   Data:       01/09/2021

# Imports necessários
import os
import PIL
import math
import numpy as np

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import array_to_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing import image_dataset_from_directory

from IPython.display import display


# Funções utilizadas no script
def constroi_modelo(upscale_factor=15, channels=1):
    conv_args = {
        "activation": "relu",
        "kernel_initializer": "Orthogonal",
        "padding": "same",
    }
    inputs = keras.Input(shape=(None, None, channels))
    x = layers.Conv2D(64, 5, **conv_args)(inputs)
    x = layers.Conv2D(64, 3, **conv_args)(x)
    x = layers.Conv2D(32, 3, **conv_args)(x)
    x = layers.Conv2D(channels * (upscale_factor ** 2), 3, **conv_args)(x)
    outputs = tf.nn.depth_to_space(x, upscale_factor)
    
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


def abreImagem(nome):
    return PIL.Image.open(nome)


def printImagem(modelo, nome):
    imgBaixa = abreImagem(nome)
    display(imgBaixa)
    
    imgAlta = conversor_alta_resolucao(modelo, imgBaixa)
    display(imgAlta)
    
    print(f"Imagem baixa: {imgBaixa.size[0], imgBaixa.size[1]}")
    print(f"Imagem alta: {imgAlta.size[0], imgAlta.size[1]}")


# Pasta com os checkpoints e imagens
PASTA_CHECKPOINT: str = r"/home/dangelo/dev/TCC/image-resolution/src/criacao_modelo/checkpoint_15x"
ARQUIVO_CHECKPOINT: str = os.path.join(PASTA_CHECKPOINT, "meu-checkpoint")
PASTA_IMGS: str = r"/home/dangelo/Downloads/imgs_teste"


if __name__ == "__main__":

    # Construção do modelo
    modelo = constroi_modelo(upscale_factor=15, channels=1)
    modelo.load_weights(ARQUIVO_CHECKPOINT)
    print(f"Resumo do modelo:\n{modelo.summary()}")

    # Mudando o nome das HR para 3x e fazendo com x15
    lista_imagens = os.listdir(PASTA_IMGS)
    contador = 0
    for img in lista_imagens:
        caminho_img: str = os.path.join(PASTA_IMGS, img)
        
        # Se tiver "hr" no nome, mudar para "hr_3x"
        if "hr" in caminho_img:
            caminho_img_3x: str = caminho_img.replace("hr", "hr_3x")
            os.rename(src=caminho_img, dst=caminho_img_3x)
        
        # Se não tiver, quer dizer que será "lr". Processar a img
        elif "lr" in caminho_img:
            caminho_img_15x: str = caminho_img.replace("lr", "hr_15x")
            
            img_lr = abreImagem(caminho_img)
            img_hr_15x = conversor_alta_resolucao(modelo, img_lr)
            
            img_hr_15x.save(caminho_img_15x)
            
        contador += 1
        print(f"Processo executado! {contador} de {len(lista_imagens)} imagens processadas...")
