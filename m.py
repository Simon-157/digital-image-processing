import numpy as np
import matplotlib.pyplot as plt

def get_shadow(original_image):
    image = np.copy(original_image)
    for i in range (0,len(image)):
        for j in range (0,len(image[i])):
            for color in range (0,len(image[i,j])):
                if image[i,j,color] < 249:
                    image[i,j,color] = 198

    plt.imshow(image)
    plt.title("The shadow of the image")
    plt.show()
    return image


def shear_transformation(img,shadow):
    sheared_image = np.arange(12*len(img)*len(img[0])).reshape(2*len(img),2*len(img[0]) ,3)
    fused_image = np.arange(12*len(img)*len(img[0])).reshape(2*len(img),2*len(img[0]) ,3)

    for color in range (0,3):
        for i in range (0,len(img)):
            for j in range (0,len(img[i])):
                if img[i,j,color] < 249:
                        sheared_image[i,j + i,color] = shadow[i,j,color]
                        fused_image[i,j + len(img), color] = img[i,j,color]
                        fused_image[i,j + i,color] = shadow[i,j,color]
                else :
                    sheared_image[i,i,color] = 255
                    sheared_image[i,i,color] = 255

    plt.imshow(sheared_image)
    plt.title("Sheared Image")
    plt.show()

    plt.imshow(fused_image)
    plt.title("Sheared and fused image")
    plt.show()

