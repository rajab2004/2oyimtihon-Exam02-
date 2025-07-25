import json
with open("Input/students.json", "r" ) as fayl : 
    malumot = json.loads(fayl.read())
    uzun_ismlar = list(filter(lambda a : len(a['name'])> 5, malumot))
with open("Output/output13.json", "w") as yozish:
    json.dump(uzun_ismlar, yozish)
    