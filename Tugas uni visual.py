class Elektronik:
    def __init__(self, inputBarang, inputMerek, inputHarga):
         self.Barang = inputBarang
         self.Merek = inputMerek
         self.Harga = inputHarga

Barang1 = Elektronik("Komputer","HP", 3000000)
Barang2 = Elektronik("Handphone","Vivo", 2000000)

print(Barang1.Merek)
