#Wahyuni Anjar Sari D0219527
class Data():
    __items = 4 # private
 
    def __init__(self,nama_barang):
        self.nama = nama_barang
 
    def harga_barang(self,harga_barang):
       hasil = self.__items * harga_barang
       return hasil
 
gitar = Data("gitar")
print(gitar.harga_barang(850))
 
