import json 
with open("Input/students.json","r") as fayil: 
    malumot = json.load(fayil)
    tartiplangan = sorted(malumot, key=lambda a: a["name"])
with open("Output/output12.json", "w") as yozish : 
    json.dump(tartiplangan, yozish, indent=4)