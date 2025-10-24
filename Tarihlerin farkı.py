liste1 = [
    "15-01-22", "20-02-22", "10-03-22",
    "25-04-22", "05-05-22", "15-06-22"
]

liste2 = [
    "10-01-22", "15-02-22", "01-03-22",
    "20-04-22", "01-05-22", "10-06-22"
]

def tarihfark(degisken):
    sira = 0
    döngü = 3
    boş_liste = []
    for i in range(len(degisken)):
        temiz_tarih = degisken[i].split("-")

        toplam0 = 0

        for j in range(len(temiz_tarih)):
            c = sira % döngü

            deger = int(temiz_tarih[j])

            if c == 0:
                toplam0 += deger
            elif c == 1:
                toplam0 += deger * 30
            elif c == 2:
                toplam0 += deger * 365

            sira += 1

        boş_liste.append(toplam0)

    return boş_liste

fonk = tarihfark(liste1)
fonk2 = tarihfark(liste2)

for n in range(len(liste1)):
    s = fonk[n] - fonk2[n]
    print(s)