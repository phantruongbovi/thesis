import autopy
import cv2
from PIL import Image
import imagehash
import os
import time

def checkImg(name):
  # hash0 = imagehash.average_hash(Image.open('data/'+ str(name)+'.png'))
  # hash1 = imagehash.average_hash(Image.open('data/'+ str(name+1)+'.png'))
  # cutoff = 5
  # if hash0 - hash1 < cutoff:
  #   print(hash0 - hash1)
  #   os.remove('data/' + str(name+1) + '.png')
  #   return True
  # else:
  #   return False
  i1 = cv2.imread('data/' + str(name) + '.png')
  i2 = cv2.imread('data/' + str(name+1) + '.png')
  difference = cv2.subtract(i1, i2)
  b, g, r = cv2.split(difference)
  if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    os.remove('data/' + str(name+1) + '.png')
    return False
  else:
    return True
def captureI(count):
  #if count == 0:
  img = autopy.bitmap.capture_screen()
  img.save('data/' + str(count+1) + '.png')
  img = cv2.imread('data/' + str(count+1) + '.png')
  crop_img = img[75:1020, 1920:4000]
  cv2.imwrite('data/' + str(count+1) + '.png', crop_img)
  return True
  # else:
  #   img = autopy.bitmap.capture_screen()
  #   img.save('data/'+ str(count+1) +'.png')
  #   img = cv2.imread('data/' + str(count+1) + '.png')
  #   crop_img = img[75:1500, 1920:4000]
  #   cv2.imwrite('data/'+ str(count+1) +'.png', crop_img)
  #   return checkImg(count)

count = 21
while True:
  captureI(count)
  count+=1
  time.sleep(150)
