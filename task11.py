import json
with open("Input/students.json", "r") as fayl:
    malumot = json.load(fayl)
    ismlar = [student["name"] for student in malumot]
    soni = len(ismlar)
with open("Output/output11.json", "w") as yozish:
    json.dump({"o'quvchilar_soni": soni}, yozish)
