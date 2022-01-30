import random
import math
import numpy as np
import time
import csv

class Para:
  def __init__(self, name, minV, maxV):
    self.name = name
    self.minV = minV
    self.maxV = maxV

class ParaVissim:
    def __init__(self):
        self.totalPara = 14

    def init(self):
        return [Para("cc0", 1.2, 1.7),
                Para("cc1", 0.7, 3.0),
                Para("cc2", 2, 7),
                Para("maxDecelerationOwn", -6, -2),
                Para("acceptedDecelerationOwn", -1.5, -0.5),
                Para("distanceOwn", 50, 150),
                Para("maxDecelerationTrailing", -5, -1),
                Para("acceptedDecelerationTrailing", -1.5, -0.5),
                Para("distanceTrailing", 50, 150),
                Para("minimumHeadway", 0.3, 1),
                Para("safetyDistance", 0 , 1),
                Para("maxDecForCoopBraking", -5, -1),
                Para("laneChangeDistance", 150, 250),
                Para("emergencyStopDistance", 3, 7)]

    def genPara(self):
        # d = [P1, P2, P3 , ... Pn]
        # P1: [x1, x2, x3, ... , xn]
        para = self.init()
        d = []
        p = []
        temp = []
        # khoi tao tri ban dau
        for i in para:
            temp.append(random.uniform(i.minV, i.maxV))
        p.append(temp)
        for i in range(self.totalPara):
            fixvalue = random.uniform(para[i].minV, para[i].maxV)
            temp = p[i][:i] + [fixvalue] + p[i][i+1:]
            p.append(temp)
        return p

    def distanceEuclid(self, di, dj):
        # di: [P1, P2, P3, ... Pk]
        # P1: [x1, x2, x3, ... , xn]
        result = 0
        for i in di:
            for j in dj:
                result += np.linalg.norm(np.array(i)-np.array(j))
        return result

    def reduceSet(self, curr):
        scores = []
        for i in range(len(curr)):
            temp = curr.copy()
            temp[i,:] = 0
            temp[:,i] = 0
            scores.append(np.sum(temp))
        result = np.where(scores == np.amax(scores))
        return result[0][0]
        

    def getMaxDistance(self, listT):
        # T: [d12, d13, d14, ... dnn]
        result = sum(listT)
        return math.sqrt(0.5*result)



    def getSet(self, numberOfSet, targetSet):
        setSampling = []
        for i in range(numberOfSet):
            setSampling.append(self.genPara())
        curr = np.zeros((numberOfSet,numberOfSet))
        lenn = len(setSampling)
        for i in range(lenn):
            for j in range(i+1, lenn):
                result = self.distanceEuclid(setSampling[i], setSampling[j])
                curr[i][j] = result
                curr[j][i] = result
        check = numberOfSet
        while check > targetSet:
            idx = self.reduceSet(curr)
            curr = np.delete(curr, idx, 0)
            curr = np.delete(curr, idx, 1)
            setSampling = setSampling[:idx] + setSampling[idx+1:]
            check -= 1
        result = []
        for i in range(len(curr)):
            if sum(curr[i]) != 0:
                result.append(setSampling[i])
                
        return result

fields = ['cc0', 'cc1', 'cc2', 'maxDecelerationOwn', 
        'acceptedDecelerationOwn', 'distanceOwn', 'maxDecelerationTrailing', 'acceptedDecelerationTrailing',
        'distanceTrailing', 'minimumHeadway', 'safetyDistance', 'maxDecForCoopBraking',
        'laneChangeDistance', 'emergencyStopDistance']
para = ParaVissim()
start = time.time()
sampleSet = para.getSet(400, 10)
end = time.time()
print(end - start)

with open('result.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    for i in sampleSet:
        write.writerows(i)