import json
with open("Input/students.json", "r") as fail: 
    malumot = json.load(fail)
    a_dan_bohlanganlar = list(filter(lambda a : a["name"].startswith("A"), malumot))
with open("Output/output14.json", "w") as yozish:
    json.dump(a_dan_bohlanganlar, yozish)