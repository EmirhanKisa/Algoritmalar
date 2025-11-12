with open(r"C:\Users\pc\OneDrive\Masaüstü\hadiye_hoca.txt", "r", encoding="utf-8") as file: #Bu kısmı değiştirirsiniz
    metin = file.read()

Tmetin = metin.splitlines()

sozluk = {} #Bütün metin bunun içinde bu sözlük
sozluk1 = {} #Katılmayanlar bunun içinde
sozluk2 = {} #Katılanlar bunun içinde
aktif_oturum = None #Key hatası vermesin diye var

for i in Tmetin:  # i dosyadaki mevcut satır
    Kmetin = i.strip()

    if Kmetin in [f"{n}. OTURUM" for n in range(1, 16)]:
        aktif_oturum = Kmetin
        sozluk[aktif_oturum] = [Kmetin]
    elif aktif_oturum:
        sozluk[aktif_oturum].append(Kmetin)

#print(sozluk.get("2. OTURUM")) Bütün oturumu yazdırma print(sozluk.get(f"{m}. OTURUM"))
#katılanlar = sozluk["1. OTURUM"][1] İstenilen ideksi yazdırma

import re

for i in range(1, 16):
    print(f"\n{i}. OTURUM")  # Oturumu yazdırıyor

    # Katılmayanları yazdıran kod
    sozluk1[f"Katılmayanlar {i}"] = sozluk[f"{i}. OTURUM"][1]
    katilmayan_metin = sozluk1[f"Katılmayanlar {i}"]
    Katılmayanlar_list = re.findall(r"\([\w.ŞşİıÖöÜüÇçĞğ]+\)", katilmayan_metin) #Çok mübarek bir fonksiyon hem parantez içini tanıyor hem noktayı alıyor hem türkçe karakterleride alıyor.

    print(f"Katılmayanlar: {Katılmayanlar_list}")

    # Katılanları yazdıran kod
    sozluk2[f"Katılanlar {i}"] = sozluk[f"{i}. OTURUM"][2]
    katilanlar_metin = sozluk2[f"Katılanlar {i}"] # Üstekinin değişmiş verisyonu
    Katılanlar_list = re.findall(r"\([\w.ŞşİıÖöÜüÇçĞğ]+\)", katilanlar_metin)

    print(f"Katılanlar: {Katılanlar_list}")

#Bütün kodun çalışma mantığı : Önce oturumları ayırdım. Sonra Oturum birin birinci indeks satırı katılmayanları verdi mübarek fonksiyon ile kişileri tespit edip yazdırdım.
#Aynısı katılanlar içinse sadece ikinci indeks








