# Burda dinamik olayan bir yapı ile kurdum. Sonrasında ise statik halini yaptım.
liste = [2, 1, 5, 1, 3, 2]

d = 0
p1 = 0
p2 = 1
p3 = 2
dur = len(liste)

while p3 < dur:

    toplam = liste[p1] + liste[p2] + liste[p3]

    if toplam >= d:
        d = toplam

    p1 = p1 + 1
    p2 = p2 + 1
    p3 = (p3+ 1)


print(d)
