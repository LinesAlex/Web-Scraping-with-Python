import csv
import os
if not os.path.exists("./files/"):
    os.mkdir("files/")
with open("./files/test.csv", 'a') as csvFile:
    try:
        writer = csv.writer(csvFile)
        writer.writerow(('number', 'number plus 2', 'number times 2'))
        for i in range(10):
            writer.writerow((i, i+2, i*2))
    finally:
        csvFile.close()
