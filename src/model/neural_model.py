import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import sys
from src.image_model import ImageNetwork

class NeuralModel:
    #pass upscale_factor to the constructor. (later)
    def __init__(self):
        self.neural_model = self.model()

    #Network model.
    def model(self, upscale_factor = 3):
        
        #Layer de input da rede
        input_layer = keras.Input(shape=(300, 300, 1), batch_size=32,name='imagem')
        #Camadas da rede
        x = layers.Conv2D(64, 5, activation='relu',kernel_initializer = "Orthogonal", padding= "same")(input_layer)
        x = layers.Conv2D(32, 3, activation='relu',kernel_initializer = "Orthogonal", padding= "same")(x)
        x = layers.Conv2D(32, 3, activation='relu',kernel_initializer = "Orthogonal", padding= "same")(x)
        x = layers.Conv2D(1 *(upscale_factor**2), 3, activation='relu',kernel_initializer = "Orthogonal", padding= "same")(x)
        #Camada de saída
        output_layer = tf.nn.depth_to_space(x, upscale_factor)

        model = keras.Model(input_layer, output_layer, name='Model_Test')

        #model.summary()
        return model

    
    def training(self, train_dataset, valdation_dataset, input_image = ''):

        loss_fn = keras.losses.MeanSquaredError()
        optimizer = keras.optimizers.Adam(learning_rate=0.001)

        self.neural_model.compile(optimizer=optimizer,loss=loss_fn)

    
        
        self.neural_model.fit(train_dataset, steps_per_epoch=30, epochs=10, verbose=2, validation_data=valdation_dataset)

        #self.neural_model.save('modelo_de_teste_salvo.txt')


        #self.neural_model.predict(input_image, verbose=2)


