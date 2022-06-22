import time
for i in range(1):
    time.sleep(2)
print("                                                                               ")
Mode_Luas=input("Mau Menghitung Luas apa?[Segitiga, dan Persegi Panjang]: ")

if Mode_Luas==("Segitiga"):
    print("                                                                               ")
    alas=int(input("Masukan Alas segitiga: "))
    print("                                                                               ")
    tinggi=int(input("Masukan Tinggi Segitiga: "))
    Luas_Segitiga=(0.5*alas*tinggi)
    print("                                                                               ")
    print("Luas Segitiga Adalah: "+str(Luas_Segitiga))
    
elif Mode_Luas=="Persegi Panjang":
    print("                                                                               ")
    panjang=int(input("Masukan Panjang Persegi Panjang: "))
    print("                                                                               ")
    lebar=int(input("Masukan Lebar Persegi Panjang: "))
    print("                                                                               ")
    tinggi=int(input("Masukan Tinggi Persegi Panjang: "))
    Luas_Persegi_Panjang=(panjang*lebar*tinggi)
    print("                                                                               ")
    print("Luas Persegi Panjang Adalah: "+str(Luas_Persegi_Panjang))
else:
    print("Bangunan Yang Anda Masukan Tidak Valid")
    for i in range(1):
        time.sleep(2)
    print("                                                                               ")
    print("Silahkan Gunakan Huruf Kapital di Awal Kalimat")
    for i in range(1):
        time.sleep(2)
    print("                                                                               ")
    print("Gunakan 'Kata Bangunan' Yang Sesuai")
    for i in range(1):
        time.sleep(2)
    print("                                                                               ")
    print("Contoh: Segitiga atau Persegi[spasi]Panjang")