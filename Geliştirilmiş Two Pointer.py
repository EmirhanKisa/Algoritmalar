"""
Bu çözüm yöntemi küçükten büyüğe sıralanmış listeler için hem hızlı hemd e bellekte yer tutmaz.
Ben uzun bir listeyi sıralamaya kalkarsam işlem maliyeti vardır ve uzun sürebilir.
"""
liste = [2, 7, 11, 15]
hedef = 9

p1 = 0
p2 = len(liste) - 1

while p1 < p2:

    toplam = liste[p1] + liste[p2]

    if toplam == hedef:
        print(f"Birinci index {p1} , İkinci index ise {p2}")
        break

    elif toplam < hedef:
        p1 = p1 + 1 # p1'i sağa kaydır

    else: # toplam > hedef

        p2 = p2 - 1 # p2'yi sola kaydır


