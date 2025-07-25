with open("Input/numbers.txt", "r") as fayl:
    sonlar = list(map(int, fayl.read().split()))
    eng_katta_son = max(sonlar)
with open("Output/output09.txt", "w") as yozish:
    yozish.write(str(eng_katta_son))