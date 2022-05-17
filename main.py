import numpy as np 
import cv2 
from matplotlib import pyplot as plt  
import time
from ij import IJ as imj

"""implementando Canny Edges
edges = cv2.Canny(img1, 50, 240)

mostrando a imagem
cv2_imshow(edges)"""

preto = (0, 0, 0)


# def showImage(img):
#     plt.imshow(img)
#     plt.show()

# def main():
#     se = cv2.imread("images/MRC 6C 2um.tif")
#     thresh, se_thresh = cv2.threshold(se, 60, 255, cv2.THRESH_BINARY)
#     # frame1 = se[0:1750, 0:2030]
#     # teste = imj.run(se, "Duplicate...")
#     #desenha o retângulo com borda amarela
#     se = cv2.rectangle(se, (10, 70), (90, 190), amarelo)
#     # cv2.imshow("Canvas", se)
#     showImage(se)

    

# main()

# Exibe a imagem na janela existente
# cv2.imshow("imagem", frame)
# cv2.waitKey(0)

# Lendo a imagem, convertendo BGR to RGB
frame = cv2.cvtColor(cv2.imread("images/MRC 6C 2um.tif"), cv2.COLOR_BGR2RGB)

# Altera o tamanho da imagem para o desejado
frame = cv2.resize(frame, (880, 780))

# desenha o retângulo com borda preta
frame = cv2.rectangle(frame, (0, 730), (879, 779), preto, -1)

cv2.imshow("canvas", frame)

frame = imj.run(frame, "Gray Scale Attribute Filtering", "operation=Opening attribute=Area minimum=20000 connectivity=4");

cv2.imshow("canvas", frame)

# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.erode(frame,kernel,iterations = 1)
# opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)

# thresh, se_thresh = cv2.threshold(se, 60, 255, cv2.THRESH_BINARY)


cv2.imshow("canvas", frame)
# print(frame.dtype)
# cv2.waitKey(0)
# cv2.imshow("canvas", opening)
# cv2.waitKey(0)