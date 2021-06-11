import os
import tensorflow as tf
import numpy as np

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import array_to_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing import image_dataset_from_directory

from PIL import Image

from IPython.display import display

#Changed the name of the class because can interfer with other library classes
class ImageNetwork:
	def __init__(self):
		# self.path_image = path_image  # Seta o caminho da imagem (str)
		# self.image = image  # Seta a imagem (PIL.Image)
		pass
		
	#Right way ?
	def image_to_array(self):  # (numpty.array)
		pass
    #Right way ?
	def array_to_image(self):  # (PIL.Image)
		pass

	#só passar o diretorio de teste ou de treino quando for utilizar nos modelos
	def dataset_create(self, directory):

		_directory = directory
		#1 imagem em cada lote, porém utilizando apenas 5 imagens, logo cada lote ira possuir apenas uma unica imagem
		dataset_build = image_dataset_from_directory(
			_directory,
			image_size=(300, 300),
			batch_size= 32,
			label_mode=None,
			color_mode="grayscale"
		)
		
		#printando informações do primeiro lote de imagens do dataset
		'''for batch in dataset_build: #para cada lote no dataset
			for img in batch:	  #para cada imagem do lote	
				imagem = array_to_img(img) #transformando uma imagem do lote em uma imagem PIL
				imagem.show()
				print(type(imagem))
				break
			break'''
		
		return dataset_build

	def validation_dataset(self, directory):

		dataset_build = image_dataset_from_directory(
			directory,
			image_size=(300, 300),
			batch_size= 5,
			label_mode=None,
			color_mode="grayscale"
		)

		'''for batch in dataset_build: #para cada lote no dataset
			for img in batch:	  #para cada imagem do lote	
				imagem = array_to_img(img) #transformando uma imagem do lote em uma imagem PIL
				imagem.show()
				print(type(imagem))
				break
			break'''

		return dataset_build