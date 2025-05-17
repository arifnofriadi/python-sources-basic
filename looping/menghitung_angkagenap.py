# menghitung angka genap

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

jumlah_genap = 0

for data in angka:
    if data % 2 == 0:
        jumlah_genap += 1

print(f'Jumlah angka genap adalah {jumlah_genap}')
