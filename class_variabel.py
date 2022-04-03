#Wahyuni Anjar Sari D0219527
class biodata():
    alamat = "Mamuju"
 
    def __init__(self, input_nama):
        self.nama = input_nama # public
 
nama = biodata("wahyuni anjar sari")
 
print(biodata.alamat)
print(nama.nama)
