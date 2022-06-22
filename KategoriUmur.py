print("Selamat Datang di Klasifikasi Umur")

Nama=input("Masukan Nama Anda: ")

Gender=input("Masukan Gender Anda (Male/Female): ")

Umur=int(input("Masukan Umur Anda: "))

print("Nama Anda Adalah: "+str(Nama))

print("Gender Anda Adalah: "+str(Gender))

if Umur >=0 and Umur <1:
    print("Kategori Umur Anda: Bayi")
    
elif Umur >=1 and Umur <10:
    print("Kategori Umur Anda: Anak-Anak")
    
elif Umur >=10 and Umur <19:
    print("Kategori Umur Anda: Remaja")
    
elif Umur >=19 and Umur <60:
    print("Kategori Umur Anda: Dewasa")
    
elif Umur >=60 and Umur <150:
    print("Kategori Umur Anda: Lansia")
    
else:
    print("Invalid Input")