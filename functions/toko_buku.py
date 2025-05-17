# Fungsi untuk menghitung total harga sebelum diskon
def hitung_harga_sebelum_diskon(jumlah_buku_A, jumlah_buku_B, jumlah_buku_C):
    harga_A = 25000  
    harga_B = 30000  
    harga_C = 35000  
    
    total_harga = (jumlah_buku_A * harga_A) + (jumlah_buku_B * harga_B) + (jumlah_buku_C * harga_C)
    return total_harga

# Fungsi untuk menghitung diskon berdasarkan jumlah buku
def hitung_diskon(jumlah_buku):
    if jumlah_buku >= 10:
        return 0.20  
    elif jumlah_buku >= 5:
        return 0.10 
    else:
        return 0 

# Fungsi utama untuk menghitung total harga setelah diskon
def hitung_harga_akhir(jumlah_buku_A, jumlah_buku_B, jumlah_buku_C):
    total_harga = hitung_harga_sebelum_diskon(jumlah_buku_A, jumlah_buku_B, jumlah_buku_C)
    total_buku = jumlah_buku_A + jumlah_buku_B + jumlah_buku_C
    diskon = hitung_diskon(total_buku)
    harga_akhir = total_harga * (1 - diskon)
    
    return harga_akhir

jumlah_buku_A = int(input("Masukkan jumlah buku A: "))
jumlah_buku_B = int(input("Masukkan jumlah buku B: "))
jumlah_buku_C = int(input("Masukkan jumlah buku C: "))

harga_akhir = hitung_harga_akhir(jumlah_buku_A, jumlah_buku_B, jumlah_buku_C)
print(f"Total harga yang harus dibayar adalah: Rp {harga_akhir:,.0f}")
