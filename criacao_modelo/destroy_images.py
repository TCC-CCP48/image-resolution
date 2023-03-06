# coding: UTF-8
#
#   Project:    TCC
#   Objective:  Deteriorate some images from the directories to make an different directory with worse resolution images.
#   Author:     Daniel D'Angelo / Leonardo Soares
#   Date:       07/22/2021

# Necessary imports
import os
import PIL.Image


# Factor choosed to decreased the resolution of the images (400x400 -> 200x200)
factor: int = 2


#################################  GETTING PATHS  #################################

# Getting the path from the script and the origin/destiny directories
base_path: str = os.getcwd()
origin_dir: str = os.path.abspath(os.path.join(base_path, "train_images"))
destiny_dir: str = os.path.abspath(os.path.join(base_path, "deteriored_images"))


###########################  ITERATING OVER THE FILES  ############################
for path_image in os.listdir(origin_dir):

    # Getting the original path from image
    original_path_image: str = os.path.abspath(os.path.join(origin_dir, path_image))

    # Creating the image object and getting its dimension
    image: PIL.Image = PIL.Image.open(original_path_image)
    height: int = image.height
    width: int = image.width

    # Resizing the image
    image = image.resize(size=(width // factor, height // factor), resample=PIL.Image.BICUBIC)

    # Creating the destination path = path_image + "_deteriored"
    new_name_image: str = path_image.replace(".png", "_deteriored")
    final_path_image = os.path.abspath(os.path.join(destiny_dir, new_name_image))

    # Saving the image resized with its quality deteriored
    image.save(fp=final_path_image, format="JPEG", quality=20)

print("Finished!")
