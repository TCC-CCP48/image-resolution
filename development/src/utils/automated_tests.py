import os
from PIL import *
from PIL.Image import Image
from utilsNeuralNetwork import *

class AutomatedTests:

	def __init__(self) -> None:
		self.modelo = constroi_modelo()

	def get_all_images_path(self, images_path: str) -> list:
		'''
		Method to get all images from an specific path
		- `Param`: path where the images are located
		- `return`: List with all images path and name
		'''
		images_path_list = []
		for dirpath, dirname, filenames in os.walk(images_path):
			for filename in filenames:
				images_path_list.append(os.path.join(dirpath,filename))

		return images_path_list


	def check_image_pixels(self) -> None:
		# redimensionaImagem()
		'''
		Method used to get the pixels difference between low resolution image and high resolution image
		- `return`: None
		'''
		images_path_list  = self.get_all_images_path('/home/leonardo/gitViews/image-resolution/images')
		PWD = os.getenv('PWD')
		low_image_resolution = ""
		high_image_resolution = ""

		for image in images_path_list:
			low_image_resolution = PIL.Image.open(image)
			high_image_resolution = conversor_alta_resolucao(self.modelo, low_image_resolution)

			with open(f"{PWD}/src/test_results/amount_pixels.txt", 'a') as f:
				f.write(f'Original image size: {low_image_resolution.size[0]}x{low_image_resolution.size[1]} and image with upscale factor 8: {high_image_resolution.size[0]}x{high_image_resolution.size[1]} \n\n')


	def constroi_modelo(self, fatorUpscale=8, canais=1) -> object:
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





if __name__ == "__main__":
	testes = AutomatedTests()
	
	testes.check_image_pixels()
