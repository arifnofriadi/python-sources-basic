kontak = {
    "Budi": "08123456789",
    "Andi": "08123456789",
    "Joko": "08123456789"
}

# tambah kontak
kontak["Joni"] = "08123456789"

# tampilkan semua kontak
for nama, nomor in kontak.items():
    print(f"{nama}: {nomor}")