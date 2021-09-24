import matplotlib.pyplot as plt
import json

f = open('23092021/2/end.json')
data = json.load(f)
arr = []
binA = []
for i in data:
    arr.append(data[i]['Total'])
    binA.append(int(i))
f.close()
print(arr)

plt.xlabel("Số xe")
plt.ylabel("Tần số xuất hiện")
plt.hist(arr,bins='auto', edgecolor="black")
plt.show()