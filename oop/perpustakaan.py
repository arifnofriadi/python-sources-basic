class Buku:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Buku {self.title}, dikarang oleh {self.author}")

buku = Buku('Laskar Pelangi', 'Andrea Hirata')
buku.info()