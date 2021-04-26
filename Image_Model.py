def image_to_array(self):  # (numpty.array)
    print('De imagem para array')


def array_to_image(self):  # (PIL.Image)
    print('De array para imagem')


class Image:
    def __init__(self, path_image, image):
        self.path_image = path_image  # Seta o caminho da imagem (str)
        self.image = image  # Seta a imagem (PIL.Image)
