import csv
import json

with open('mycsv1.csv', 'w', newline='') as f:
    fieldnames = ['Time', 'Car', 'Motobike', 'Truck', 'Bicycle', 'Total']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    f = open('23092021/1/end.json')
    data = json.load(f)
    for i in data:
        thewriter.writerow({
            'Time' : i,
            'Car': data[i]['Car'],
            'Motobike': data[i]['Motobike'],
            'Truck' : data[i]['Truck'],
            'Bicycle' : data[i]['Bicycle'],
            'Total' : data[i]['Total']
        })
    f.close()