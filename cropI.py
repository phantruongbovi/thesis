
import numpy as np
import cv2


count = 1
while count <= 271:
    img = cv2.imread('data/'+str(count)+'.png')
    crop_img1 = img[0:425, 0:950] # Le Dai Hanh 2
    crop_img2 = img[0:425,950:1919] # Ly Thuong Kiet 2
    crop_img3 = img[496:944, 0:942] #3 thang 2 Ly Thai To
    crop_img4 = img[496:944, 954:1919] # 3 thang 2 Su van hanh
    cv2.imwrite('23092021/1/' + str(count) + '.png', crop_img1)
    cv2.imwrite('23092021/2/' + str(count) + '.png', crop_img2)
    cv2.imwrite('23092021/3/' + str(count) + '.png', crop_img3)
    cv2.imwrite('23092021/4/' + str(count) + '.png', crop_img4)
    count+=1