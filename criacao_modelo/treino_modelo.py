#   coding:utf-8
#
#   Arquivo:    treino_modelo.py
#   Objetivo:   montar um script que treine a rede neural já com as 10 mil imagens, de 34 em 34 épocas.
#   Autores:    Caroline, Daniel, Leonardo, Paloma
#   Turma:      CC8P48 / CC7P48
#   Data:       05/08/2020

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

# Definicão de classes e funções importantes para o programa
PASTA_CHECKPOINT: str = "./checkpoint/"
ARQUIVO_CHECKPOINT: str = "./checkpoint/meu-checkpoint"


##################################  CLASSES E FUNÇÕES UTILIZADAS  #################################

class ModeloCallback(keras.callbacks.Callback):
    def __init__(self, fator_escala, caminho_imagens_teste):
        super(ModeloCallback, self).__init__()
        self.img_teste = coleta_img_baixa_resolucao(
            load_img(caminho_imagens_teste[0]), fator_escala
        )

    # Método herdado de keras.callbacks.Callback
    def on_epoch_begin(self, epoch, logs=None):
        self.psnr = []

    # Método herdado de keras.callbacks.Callback
    def on_epoch_end(self, epoch, logs=None):
        print("Média da métrica PSNR por época: %.2f" % (np.mean(self.psnr)))

    # Método herdado de keras.callbacks.Callback
    def on_test_batch_end(self, batch, logs=None):
        self.psnr.append(10 * math.log10(1 / logs["loss"]))



def redimensionar(array_img):
    return array_img / 255


def processa_entrada(imagem, tamanho_entrada):
    return tf.image.resize(imagem, [tamanho_entrada, tamanho_entrada], method="area")


def coleta_img_baixa_resolucao(img, fator):
    return img.resize(
        (img.size[0] // fator, img.size[1] // fator),
        PIL.Image.BICUBIC,
    )


def constroi_modelo(upscale_factor=3, channels=1):
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


################################  SCRIPT PARA TREINO DO MODELO  ################################
def treino(modelo, pastaCheckpoint):
    
    # ATENÇÃO: ALTERAR O CAMINHO ABAIXO PARA AS RESPECTIVAS PASTAS
    #   Organização das pastas:
    #   dir_principal
    #       |
    #       |--------treino
    #       |           |
    #       |           |--- imgtreino0.png
    #       |           |---      ...
    #       |           |--- imgtreino7999.png
    #       |
    #       |--------validacao
    #       |           |
    #       |           |--- imgvalidacao0.png
    #       |           |---     ...
    #       |           |--- imgvalidacao999.png
    #       |
    #       |--------teste
    #       |           |
    #       |           |--- imgteste0.png
    #       |           |---      ...
    #       |           |--- imgteste999.png
    #
    dir_principal = r"/home/dangelo/dev/TCC/image-resolution/images"

    # Definição de algumas constantes usadas no programa
    TAMANHO_RECORTE: int = 300
    FATOR_UPSCALE: int = 3
    TAMANHO_IMAGEM_ENTRADA = TAMANHO_RECORTE // FATOR_UPSCALE
    LOTE: int = 8
    EPOCAS: int = 34
    PORCENTAGEM_VALIDACAO: float = 0.1
    ARQUIVO_CHECKPOINT: str = os.path.join(pastaCheckpoint, "meu-checkpoint")

    # Criação dos datasets: treino e validação
    ds_treino = image_dataset_from_directory(
        directory=dir_principal,
        batch_size=LOTE,
        image_size=(TAMANHO_RECORTE, TAMANHO_RECORTE),
        validation_split=PORCENTAGEM_VALIDACAO,
        color_mode="grayscale",
        subset="training",
        seed=1337,
        label_mode=None
    )

    ds_validacao = image_dataset_from_directory(
        directory=dir_principal,
        batch_size=LOTE,
        image_size=(TAMANHO_RECORTE, TAMANHO_RECORTE),
        validation_split=PORCENTAGEM_VALIDACAO,
        color_mode="grayscale",
        subset="validation",
        seed=1337,
        label_mode=None
    )

    ds_treino = ds_treino.map(redimensionar)
    ds_validacao = ds_validacao.map(redimensionar)

    # Recuperar todos os arquivos para teste
    imagens_teste = os.path.abspath(os.path.join(dir_principal, "test"))

    caminho_imagens_teste: list = []
    for imgs in os.listdir(imagens_teste):
        final_caminho: str = os.path.join(imagens_teste, imgs)
        caminho_imagens_teste.append(final_caminho)

    ds_treino = ds_treino.map(
            lambda x: (processa_entrada(x, TAMANHO_IMAGEM_ENTRADA), x)
    )
    ds_treino = ds_treino.prefetch(buffer_size=32)

    ds_validacao = ds_validacao.map(
            lambda x: (processa_entrada(x, TAMANHO_IMAGEM_ENTRADA), x)
    )
    ds_validacao = ds_validacao.prefetch(buffer_size=32)

    callback_parada_eficiencia = keras.callbacks.EarlyStopping(monitor="loss", patience=10)

    callback_checkpoint = keras.callbacks.ModelCheckpoint(
        filepath=pastaCheckpoint,
        save_weights_only=True,
        monitor="loss",
        mode="min",
        save_best_only=True,
    )

    callbacks = [ModeloCallback(FATOR_UPSCALE, caminho_imagens_teste), 
                 callback_parada_eficiencia, 
                 callback_checkpoint
                ]

    modelo.fit(
        ds_treino, epochs=EPOCAS, callbacks=callbacks, validation_data=ds_validacao, verbose=2
    )

    modelo.save_weights(ARQUIVO_CHECKPOINT)


if __name__ == "__main__":

    # Construindo modelo zerado
    modelo = constroi_modelo(3, 1)

    try:
        # Criando pasta para os checkpoints
        if not os.path.exists(PASTA_CHECKPOINT):
            os.mkdir(PASTA_CHECKPOINT)

        if os.path.exists(ARQUIVO_CHECKPOINT):
            modelo.load_weights(ARQUIVO_CHECKPOINT)
        
        treino(modelo, PASTA_CHECKPOINT)

        print("Treino finalizado!")

    except FileExistsError:
        print("Arquivo já existe!")
