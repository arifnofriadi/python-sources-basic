def total_harga(*harga): 
    print("Daftar harga: ", harga)
    total = sum(harga)
    print("Total: ", total)

total_harga(10000, 20000, 30000, 40000, 50000)