import numpy as np
import cv2
import glob

for f in glob.glob("data/*.png"):
    img = cv2.imread(f)
    filename = f[5:]
    crop_img1 = img[110:510, 0:972] # Le Dai Hanh 1
    crop_img2 = img[110:510,975:1916] # Ly Thuong Kiet 2
    crop_img3 = img[590:1080, 5:972] #3 thang 2 Ly Thai To
    crop_img4 = img[590:1080, 972:1919] # 3 thang 2 Su van hanh
    cv2.imwrite('27012022/LDH1/' + filename, crop_img1)
    cv2.imwrite('27012022/LDH2/' + filename, crop_img2)
    cv2.imwrite('27012022/LTK2/' + filename, crop_img3)
    cv2.imwrite('27012022/LTK3/' + filename, crop_img4)
            