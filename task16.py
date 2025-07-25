import csv
with open("Input/grades.csv","r") as fayl:
    oqish = csv.reader(fayl)
    baholar = list(oqish)
    bahosi_5 = (filter(lambda b:b[1] == "5", baholar))
hammasi = len(list(bahosi_5))
with open("Output/output16.txt", "w") as yozish:
    yozish.write(f"Bahosi 5 bo'lganlar soni: {hammasi}\n")
    yozish.write("Bahosi 5 bo'lganlar:\n")
    for baho in bahosi_5:
        yozish.write(f"{baho[0]} - {baho[1]}\n")
      