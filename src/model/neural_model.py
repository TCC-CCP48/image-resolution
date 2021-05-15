import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class NeuralModel:

    def __init__(self):
        self.model()

    #Network model.
    def model(self, upscale_factor = 3):
        
        #Layer de input da rede
        input_layer = keras.Input(shape=(300, 300, 1), batch_size=32,name='imagem')
        #Camadas da rede
        x = layers.Conv2D(64, 5, activation='relu')(input_layer)
        x = layers.Conv2D(64, 3, activation='relu')(x)
        x = layers.Conv2D(32, 3, activation='relu')(x)
        #Camada de saída
        output_layer = layers.UpSampling2D(upscale_factor)(x)

        model = keras.Model(input_layer, output_layer, name='Model_Test')

        model.summary()

teste = NeuralModel()
