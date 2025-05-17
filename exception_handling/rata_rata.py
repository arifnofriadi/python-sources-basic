import statistics

try:
    angka = [30, 40, 50]
    print('Rata-rata = ', statistics.mean(angka))
except (ZeroDivisionError, ValueError) as e:
    print('Inputan harus berupa angka dan tidak boleh 0 - ', e)
finally:
    print('Proses Selesai')