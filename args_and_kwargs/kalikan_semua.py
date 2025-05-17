def kalikan_semua(*data):
    hasil = 1
    for angka in data:
        hasil *= angka
    return hasil

print(kalikan_semua(3,4,2))