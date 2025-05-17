# Seorang anak ingin menaiki tangga dengan total 50 anak tangga. 
# Ia hanya bisa melangkah 1 atau 2 anak tangga dalam sekali langkah. 
# Buat program yang menghitung berapa banyak kemungkinan cara anak tersebut bisa mencapai puncak tangga.

def hitung_tangga(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    langkah_1, langkah_2 = 1, 2
    count = 0
    i = 3

    while i <= n:
        count = langkah_1 + langkah_2
        langkah_1 = langkah_2
        langkah_2 = count
        i += 1

    return count

anak_tangga = 50
hasil = hitung_tangga(anak_tangga)
print(f"Banyak cara untuk mencapai puncak tangga dengan {anak_tangga} anak tangga adalah {hasil:,}")