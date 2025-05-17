uang_kembalian = int(input("Masukkan uang kembalian: "))
pecahan = [50000, 5000, 1000]
kembalian = {}

while uang_kembalian > 0: 
    for uang in pecahan:
        if uang_kembalian >= uang:
            jumlah_lembar = uang_kembalian // uang
            kembalian[uang] = jumlah_lembar
            uang_kembalian %= uang
        
print("Uang kembalian:")
for uang, jumlah in kembalian.items():
    print(f"Uang Rp {uang} berjumlah {jumlah} lembar")

        