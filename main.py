import numpy as np 
import cv2 
from matplotlib import pyplot as plt  
import time
# from ij import IJ as imj

"""implementando Canny Edges
edges = cv2.Canny(img1, 50, 240)

mostrando a imagem
cv2_imshow(edges)"""

def showImage(img):
    plt.imshow(img)
    plt.show()

def main():
    se = cv2.imread("images/MRC 6C 2um.tif")
    thresh, se_thresh = cv2.threshold(se, 60, 255, cv2.THRESH_BINARY)
    showImage(se)
    

main()

# imj.OpenImage("C:/Users/Matheus/Desktop/arquivos_Matheus/estagio/imagens-gsr/mrc-6c-2um/se/MRC 6C 2um.tif")