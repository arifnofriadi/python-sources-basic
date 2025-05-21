# membuat class dan object

class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def jalan(self):
        print(f"Mobil {self.merk} berwarna {self.warna} sedang berjalan")

mobil = Mobil("Toyta", "Merah")
mobil.jalan()