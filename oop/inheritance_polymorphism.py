class Hewan:
    def bersuara(self):
        print("Hewan bersuara")

class Anjing(Hewan):
    def bersuara(self):
        print('Guk guk!')

class Kucing(Hewan):
    def bersuara(self):
        print('Miau miau!')

def tes_suara(hewan):
    hewan.bersuara()

anjing = Anjing()
kucing = Kucing()

tes_suara(anjing)
tes_suara(kucing)