# cetak angka ganjil dengan for loop
print("Perulangan angka ganjil")

awal = int(input("Masukkan angka awal: "))
akhir = int(input("Masukkan angka akhir: "))
print('\n')

for i in range(awal, akhir):
    if i % 2 == 1:
        print(f'Angka ganjil: {i}')