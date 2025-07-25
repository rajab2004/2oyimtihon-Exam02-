with open("Input/numbers.txt", "r") as fayl:
    sonlar = list(map(int, fayl.read().split()))
    tartiblangan_sonlar = sorted(sonlar)
with open("Output/output10.txt", "w") as yozish:
    yozish.write(" ".join(map(str, tartiblangan_sonlar)))