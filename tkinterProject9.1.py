# Learning to create image lists:
# import the modules
import os

i = 0
image_list = []
# get the path/directory
folder_dir = r".\images"

for images in os.listdir(folder_dir):
    # check if the image ends with png or...
    if (images.endswith(".png") or
            images.endswith(".jpg") or
            images.endswith(".jpeg") or
            images.endswith(".jfif")):

        # .append helps input the image name into list!
        image_list.append(images)
        print(i, '.', images)
        i = i+1
        print(image_list)