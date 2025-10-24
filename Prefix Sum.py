liste = [1, 2, 3, 4]
d = 0
cevap_listesi = []

for i in range(len(liste)):

    d = liste[i] + d
    cevap_listesi.append(d)

print(cevap_listesi)