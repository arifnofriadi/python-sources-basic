def info_pemesanan(*item_satu, **item_dua):
    print("Pesanan tambahan: ", item_satu)
    print("Detail pesanan: ")
    for key, value in item_dua.items():
        print(f"{key.capitalize()}: {value}")

info_pemesanan("sambal", "kerupuk", makanan="Pecel lele", minuman="Teh Hangat")