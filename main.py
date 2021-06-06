#from image_model import ImageNetwork
from src.image_model import ImageNetwork
from src.model.neural_model import NeuralModel
import tensorflow as tf

objeto = ImageNetwork()

#objeto.dataset_create('src/images_train/')

#objeto.validation_dataset('src/images_validation')

print(__name__)
print(f'versão do tensorflow printando aqui no main!!!!!! {tf.version.VERSION}')
treino = objeto.dataset_create('src/images_train/')

validacao = objeto.validation_dataset('src/images_validation')

teste = NeuralModel().train(treino, validacao)

