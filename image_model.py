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


	def dataset_create(self):
		# Training dataset
		#Missing batch size
		train_ds = image_dataset_from_directory(
			"images_train/",
			image_size=(300, 300),
			label_mode=None,
			color_mode="grayscale",
		)
		#Testing dataset
		test_ds = image_dataset_from_directory(
			"images_train/",
			image_size=(300,300),
			label_mode=None,
			color_mode="grayscale"
		)
		
		#A função image_dataset_from_directory retorna um objeto tf.data.Dataset.
		#https://keras.io/api/preprocessing/image/
		#https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image_dataset_from_directory

		print(train_ds)

