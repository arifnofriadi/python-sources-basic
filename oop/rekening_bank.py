class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo

    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"Saldo {self.nama} sekarang sebesar {self.saldo}")

    def tarik(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            print(f"Penarikan berhasil. Sisa saldo {self.saldo}")
        else:
            print("Penarikan gagal. Saldo tidak mencukupi.")

akun = RekeningBank("Arif", 1000000)
akun.setor(500000)
akun.tarik(200000)