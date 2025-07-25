with open("Input/numbers.txt", "r") as fayl:
    sonlar = list(map(int, fayl.read().split()))
    yigindi = sum(sonlar)
with open("Output/output08.txt", "w") as yozish:
    yozish.write(str(yigindi))