daftar_belanja = []

# tambahkan item
daftar_belanja.append("minyak goreng")
daftar_belanja.append("daging")
daftar_belanja.append("telur")
daftar_belanja.append("beras")

# hapus item tertentu
if 'daging' in daftar_belanja:
    daftar_belanja.remove('daging')

# tampilkan daftar belanja
for data in daftar_belanja:
    print(f"- {data}")