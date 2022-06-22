def luas_segitiga(alas, tinggi):
    luas= (alas* tinggi)/2
    return luas
    
print("Welcome To Triangle Calc: ")
alas=float(input("Masukan Alas: "))
tinggi=float(input("Masukan Tinggi: "))
print("Luas Segitiga Adalah: ",luas_segitiga(alas, tinggi))