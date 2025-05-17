try:
    angka = int(input('Masukkan angka : '))
    hasil = 10 / angka
    print(f'Hasil pembagian 10 / {angka} = {hasil}')
except ZeroDivisionError:
    print('Tidak bisa membagi dengan 0')
except ValueError:
    print('Inputan harus angka')
finally:
    print('Proses Selesai')