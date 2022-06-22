import time
print("                                                                               ")
for i in range(1):
    time.sleep(2)
print("Halo, Selamat Datang di Program Neil Ganteng")
print("                                                                               ")
for i in range(1):
    time.sleep(3)
print("Untuk Menghitung Luas Nya Silahkan Ketik 'Bangunan' Yang Diinginkan")
print("                                                                               ")
for i in range(1):
    time.sleep(2)
print("Di Program Ini, Anda Dapat Menghitung Luas 'Segitiga' dan 'Persegi Panjang'")
print("                                                                               ")
for i in range(1):
    time.sleep(2)
print("Selamat Mencoba !!")
print("                                                                               ")
for i in range(1):
    time.sleep(2)
Mode_Luas=input("Mau Menghitung Luas apa: ")

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