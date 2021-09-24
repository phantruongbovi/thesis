count = 1
tg = 271
f = open('Images.txt', "w")
while count <= tg:
    f.write('/content/drive/MyDrive/TLMH/LVTN/data/23092021/4/' + str(count) + ".png\n")
    count += 1

f.close()

