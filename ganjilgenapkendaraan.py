#Membuat Algoritma Pseudocode Ganjil Genap Kendaraan

print("Selamat Datang Di Program Ganjil Genap Kendaraan") #Judul

No_Kendaraan=int(input("Masukan No/plat Kendaraan: ")) #Deklarasi

if No_Kendaraan%2==0:
    print("Kendaraan Anda Termasuk Genap")          #Algoritma Untuk Kendaraan No. Genap
    print("Silahkan Parkir Di Tempat Parkir B")

elif No_Kendaraan%1==0:
    print("Kendaraan Anda Termasuk Ganjil")         #Algoritma Untuk Kendaraan No. Ganjil
    print("Silahkan Parkir DI Tempat Parkir A")
    
else:           
    print("Harap Memasukan Angka Dengan Benar")     #Algoritma Untuk Mencegah User Menginput Bukan Nomor.