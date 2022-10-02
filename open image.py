import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import json
from PIL import Image
import cv2

image = 'JNCE_2019149_20C00048_V01-raw.png'
im_info = '6879-Metadata.json'
with open(im_info, 'rb') as json_file:
    im_info_dir = json.load(json_file)

img = Image.open(image)
im_ar = np.array(img)
s1, s2 = im_ar.shape
print(im_ar)
ci = cv2.imread('JNCE_2019149_20C00028_V01-raw.png')
cv2.imshow("l", im_ar)
cv2.waitKey(0)