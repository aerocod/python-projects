print("Selamat Datang Di Kalkulator Segitiga")
print("Detail Rumus:")
print("1. Luas Segitiga")
print("2. Keliling Segitiga")
print("3. Tinggi Segitiga")
print("4. Alas Segitiga")

rumus=input("Masukan Nomor Rumus Yang Ingin Digunakan: ")

if rumus=="1":
    Alas=float(input("Masukan Alas: "))
    Tinggi=float(input("Masukan Tinggi: "))
    Luas=0.5*Alas*Tinggi
    print("Luas Segitiga Adalah: "+str(Luas))
    
elif rumus=="2":
    Sisi1=float(input("Masukan Sisi Pertama: "))
    Sisi2=float(input("Masukan Sisi Kedua: "))
    Sisi3=float(input("Masukan Sisi Ketiga: "))
    Kel=Sisi1+Sisi2+Sisi3
    print("Keliling Segitiga Adalah: "+str(Kel))
    
elif rumus=="3":
    Luass=float(input("Masukan Luas: "))
    Salas=float(input("Masukan Alas: "))
    Tinggis=2*Luass/Salas
    print("Tinggi Segitiga Adalah: "+str(Tinggis))
    
elif rumus=="4":
    L=float(input("Masukan Luas: "))
    T=float(input("Masukan Tinggi: "))
    A=2*L/T
    print("Alas Segitiga Adalah: "+str(A))
    
else:
    print("Invalid Input")
    