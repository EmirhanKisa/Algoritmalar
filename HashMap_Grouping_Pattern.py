dosyalar = ["tatil.jpg", "odev.pdf", "manzara.jpg", "fatura.pdf", "logo.png"]
grup = {}

for i in dosyalar:
    uzanti = i.split(".")[1]

    if uzanti not in grup:
        grup[uzanti] = []

    grup[uzanti].append(i)

print(grup)