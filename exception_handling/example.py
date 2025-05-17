data = [1, 2, 3]

try:
    print(data[5])
except IndexError as e:
    print('Indeks tidak ditemukan : ', e)

my_dict = {
    'nama': 'Arif'
}

try:
    print(my_dict['alamat'])
except KeyError as e:
    print('Indeks tidak ditemukan : ', e)

try:
    angka = int("abc")
except (ValueError, TypeError) as e:
    print('Terjadi kesalahan : ', e)