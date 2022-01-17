import autopy
import cv2
from PIL import Image
import imagehash
import os
import time
from datetime import datetime

def checkImg(name):
  i1 = cv2.imread('data/' + str(name) + '.png')
  i2 = cv2.imread('data/' + str(name+1) + '.png')
  difference = cv2.subtract(i1, i2)
  b, g, r = cv2.split(difference)
  if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    os.remove('data/' + str(name+1) + '.png')
    return False
  else:
    return True
def captureI():
  #if count == 0:
  now = datetime.now()
  current_time = now.strftime("%H:%M")
  img = autopy.bitmap.capture_screen()
  img.save('data/' + current_time + '.png')
  img = cv2.imread('data/' + current_time + '.png')
  crop_img = img[0:1080, 1920:4000]
  cv2.imwrite('data/' + current_time + '.png', crop_img)
  
  return True
  # else:
  #   img = autopy.bitmap.capture_screen()
  #   img.save('data/'+ str(count+1) +'.png')
  #   img = cv2.imread('data/' + str(count+1) + '.png')
  #   crop_img = img[75:1500, 1920:4000]
  #   cv2.imwrite('data/'+ str(count+1) +'.png', crop_img)
  #   return checkImg(count)

a = False
while True:
  # if a == False:
  #   time.sleep(5)
  #   a = True
  captureI()
  #count+=1
  time.sleep(60)
