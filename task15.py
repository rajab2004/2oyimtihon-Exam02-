import csv
with open("Input/grades.csv", "r") as fayl:
    oqish = csv.reader(fayl)
    next(oqish)  
    eng_yuqori_baho = 0
    eng_yuqori_oquvchi = ""
    for baho in oqish:
        if int(baho[1]) > eng_yuqori_baho:
            eng_yuqori_baho = int(baho[1])
            eng_yuqori_oquvchi = baho[0]
with open("Output/output15.txt", "w") as yozish:
    yozish.write(f"Eng yuqori baho: {eng_yuqori_baho}\n")
    yozish.write(f"Eng yuqori baho olgan o'quvchi: {eng_yuqori_oquvchi}\n")