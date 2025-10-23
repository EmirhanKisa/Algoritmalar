dizi = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 2
n = len(dizi) # 10

mevcut = sum(dizi[:k])
toplam = mevcut

for i in range(k,n):

    mevcut = mevcut - dizi[i-k] + dizi[i]

    toplam = max(toplam, mevcut)

print(toplam)