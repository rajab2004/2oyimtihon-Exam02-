def so_zlar_qaytariq(matn):
    so_zlar = matn.split()
    natija = {}
    for so_z in so_zlar:
        natija[so_z] = natija.get(so_z, 0) + 1
    return natija
matn = "salom salom dunyo"
natija = so_zlar_qaytariq(matn)
print(natija)  # {'salom': 2, 'dunyo':
