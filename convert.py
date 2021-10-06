import csv
import json

with open('mycsv1.csv', 'w', newline='') as f:
    fieldnames = ['Time', 'Car', 'Motobike', 'Truck', 'Bicycle', 'Total']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    f = open('23092021/4/end.json')
    data = json.load(f)
    for i in data:
        thewriter.writerow({
            'Time' : i,
            'Car': int(float(data[i]['Car'])*100),
            'Motobike': int(float(data[i]['Motobike'])*100),
            'Truck' : int(float(data[i]['Truck'])*100),
            'Bicycle' : int(float(data[i]['Bicycle'])*100),
            'Total' : int(float(data[i]['Total'])*100)
        })
    f.close()
