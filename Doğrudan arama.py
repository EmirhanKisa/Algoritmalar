# Kodun amacı : Bir listemiz var ve girilen input değerinin listedeki indeks değerini buluyoruz. Yoksa nerde olması gerektiğini.
list = [1,3,5,6,9]

hedef = int(input("Hedef seçiniz: "))
indeks = 0

for i in list:# i = listedeki her sayı

    if i == hedef:
        print(f"İndeks değeri {indeks}")
        break

    elif i > hedef:
        print(f"İndeks değeri {indeks}")
        break

    indeks = indeks + 1
else:
    print(f"İndeks değeri {indeks}")



