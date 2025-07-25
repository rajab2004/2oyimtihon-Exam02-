def fish_tartibini_ozgartir(fish):
    qismlar = fish.split()
    if len(qismlar) == 3:
        familiya, ism, sharif = qismlar
        natija = f"{ism} {sharif}, {familiya}"
        return natija
    else:
        return " Iltimos, FISH ni to'liq kiriting (Familiya Ism Sharif)."
fish = input("FISH ni kiriting (Familiya Ism Sharif): ")
natija = fish_tartibini_ozgartir(fish)
print(natija)
