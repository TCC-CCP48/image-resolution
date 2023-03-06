#   coding:utf-8
#
#   Arquivo:    keras_docker.py
#   Objetivo:   montar um script que treine a rede neural já com as 10 mil imagens.
#   Autores:    Caroline, Daniel, Leonardo, Paloma
#   Turma:      CC8P48 / CC7P48
#   Data:       02/08/2020


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
dir_principal = r"/home/dangelo/dev/TCC/image-resolution/src/images_keras_docker"

# Definição de algumas constantes usadas no programa
TAMANHO_RECORTE: int = 512
FATOR_UPSCALE: int = 3
TAMANHO_IMAGEM_ENTRADA = TAMANHO_RECORTE // FATOR_UPSCALE
LOTE: int = 8
EPOCAS: int = 100
PORCENTAGEM_VALIDACAO: float = 0.1


##################################  CLASSES E FUNÇÕES UTILIZADAS  #################################

class ModeloCallback(keras.callbacks.Callback):
    def __init__(self, fator_escala):
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


def constroi_modelo(fator_escala=3, canais=1):
    config_convnet = {
        "activation": "relu",
        "kernel_initializer": "Orthogonal",
        "padding": "same",
    }
    inputs = keras.Input(shape=(None, None, canais))
    x = layers.Conv2D(64, 5, **config_convnet)(inputs)
    x = layers.Conv2D(64, 3, **config_convnet)(x)
    x = layers.Conv2D(32, 3, **config_convnet)(x)
    x = layers.Conv2D(canais * (fator_escala ** 2), 3, **config_convnet)(x)
    outputs = tf.nn.depth_to_space(x, fator_escala)
    return keras.Model(inputs, outputs)


def coleta_img_baixa_resolucao(img, fator):
    return img.resize(
        (img.size[0] // fator, img.size[1] // fator),
        PIL.Image.BICUBIC,
    )


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
imagens_teste = os.path.abspath(os.path.join(dir_principal, "teste"))

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

pasta_checkpoint = "/tmp/checkpoint"

callback_checkpoint = keras.callbacks.ModelCheckpoint(
    filepath=pasta_checkpoint,
    save_weights_only=True,
    monitor="loss",
    mode="min",
    save_best_only=True,
)

modelo = constroi_modelo(fator_escala=FATOR_UPSCALE, canais=1)
modelo.summary()

callbacks = [ModeloCallback(FATOR_UPSCALE), callback_parada_eficiencia, callback_checkpoint]
loss_fn = keras.losses.MeanSquaredError()
otimizador = keras.optimizers.Adam(learning_rate=0.001)

numero_epocas = 100

modelo.compile(
    optimizer=otimizador, loss=loss_fn,
)

modelo.fit(
    ds_treino, epochs=numero_epocas, callbacks=callbacks, validation_data=ds_validacao, verbose=2
)

modelo.load_weights(pasta_checkpoint)


total_bicubic_psnr = 0.0
total_test_psnr = 0.0

for _, caminho_img_teste in enumerate(caminho_imagens_teste[50:150]):
    
    img = load_img(caminho_img_teste)
    entrada_baixa_res = coleta_img_baixa_resolucao(img, FATOR_UPSCALE)
    
    largura = entrada_baixa_res.size[0] * FATOR_UPSCALE
    altura = entrada_baixa_res.size[1] * FATOR_UPSCALE
    
    img_alta_res = img.resize((largura, altura))
    
    img_previsao = conversor_alta_resolucao(modelo, entrada_baixa_res)
    
    img_baixa_resolucao = entrada_baixa_res.resize((largura, altura))
    
    array_baixa_res = img_to_array(img_baixa_resolucao)
    array_alta_res = img_to_array(img_alta_res)
    array_previsao = img_to_array(img_previsao)
    
    bicubic_psnr = tf.image.psnr(array_baixa_res, array_alta_res, max_val=255)
    test_psnr = tf.image.psnr(array_previsao, array_alta_res, max_val=255)

    total_bicubic_psnr += bicubic_psnr
    total_test_psnr += test_psnr
    
    print(
        "Métrica PSNR entre baixa/alta resolução nas imagens é de %.4f" % bicubic_psnr
    )
    print("Métrica PSNR entre imagem de previsão e imagem de alta resolução é de %.4f" % test_psnr)

print("Média da métrica PSNR para imagens de baixa resolução é de %.4f" % (total_bicubic_psnr / 100))
print("Média da métrica PSNR para imagens reconstruídas é de %.4f" % (total_test_psnr / 100))
