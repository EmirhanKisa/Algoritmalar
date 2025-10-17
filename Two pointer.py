# 1. index + [Değişicek]
# 2. index + [Değişicek]
liste = [2, 7, 11, 15]
hedef = 9

for i in range(len(liste)): # 4 kere dönücek

    for j in range(len(liste)):
        d = i + 1

        if liste[i] + liste[j + d] == hedef:
            print(f"Birinci index {i} , İkinci index ise {j+d}")

        else:
            pass

