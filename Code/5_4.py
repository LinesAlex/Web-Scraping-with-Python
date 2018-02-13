import csv
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, 'html.parser')

table = bsObj.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")

if not os.path.exists('./files') :
    os.mkdir('files/')
with open("./files/editors.csv", "wt", newline="", encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)
    try:
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)
    finally:
        csvFile.close()
