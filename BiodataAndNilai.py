import time
print("                                                     ")
nama=input("Masukin Nama Kamu: ")
print("                                                     ")
kelas=input("Masukin Kelas Kamu: ")
print("                                                     ")
nilai_uas=eval(input("Masukin Nilai Uas Kamu: "))
print("                                                     ")
nilai_pts=eval(input("Masukin Nilai Pts Kamu: "))
print("                                                     ")
nilai_tugas=eval(input("Masukin Nilai Tugas Kamu: "))
for i in range(1):
    time.sleep(2)
print("                                                     ")
print("Nama Kamu Adalah: "+str(nama))
for i in range(1):
    time.sleep(2)
print("                                                     ")
print("Kamu Kelas: "+str(kelas))
for i in range(1):
    time.sleep(2)
print("                                                     ")
Total_Nilai=(nilai_pts/3+nilai_tugas/3+nilai_uas/3)

if Total_Nilai >=90 and Total_Nilai <100:
    print("Nilai Rata-rata Kamu Adalah: "+str(Total_Nilai))
    for i in range(1):
        time.sleep(2)
    print("                                                     ")
    print("Grade A")
    print("Selamat Anda Lulus Dengan Nilai Yang Memuaskan")
    for i in range(1):
        time.sleep(2)
    print("Orang Tua Mu Pasti Bangga :D")
    
elif Total_Nilai >=80 and Total_Nilai <90:
    print("Nilai Rata-rata Kamu Adalah: "+str(Total_Nilai))
    for i in range(1):
        time.sleep(2)
    print("                                                     ")
    print("Grade B")
    print("Selamat Anda Lulus Dengan Nilai Yang Bagus")
    for i in range(1):
        time.sleep(2)
    print("Wah, Selamat Yahhh")    
        
elif Total_Nilai >=70 and Total_Nilai <80:
    print("Nilai Rata-rata Kamu Adalah: "+str(Total_Nilai))
    for i in range(1):
        time.sleep(2)
    print("                                                     ")
    print("Grade C")
    print("Selamat Anda Lulus Dengan Nilai Yang Cukup Bagus")
    for i in range(1):
        time.sleep(2)
    print("Mantap, Ayo Berjuang Lebih Keras")
    
elif Total_Nilai >=60 and Total_Nilai <70:
    print("Nilai Rata-rata Kamu Adalah: "+str(Total_Nilai))
    for i in range(1):
        time.sleep(2)
    print("                                                     ")
    print("Grade D")
    print("Selamat Anda Lulus Dengan Nilai Yang Cukup")
    for i in range(1):
        time.sleep(2)
    print("Kamu Sudah Bisa Sejauh ini Ayo Tingkatkan Lagi")
    
elif Total_Nilai >=50 and Total_Nilai <60:
    print("Nilai Rata-rata Kamu Adalah: "+str(Total_Nilai))
    for i in range(1):
        time.sleep(2)
    print("                                                     ")
    print("Grade E")
    print("Selamat Anda Lulus Dengan Nilai Yang Kurang Memuaskan")
    for i in range(1):
        time.sleep(2)
    print("Walaupun Kecil Tetaplah Beharga Tetaplah Berjuang")
    
elif Total_Nilai <=50:
    print("Nilai Rata-rata Kamu Adalah: "+str(Total_Nilai))
    for i in range(1):
        time.sleep(2)
    print("                                                     ")
    print("Grade F")
    print("Anda Dinyatakan Tidak Lulus, Belajarlah Lebih Giat Lagi:D")
    for i in range(1):
        time.sleep(2)
    print("Kamu Pasti Bisa Menghadapi Semua Ini:D")
else:
    print("Invalid Input")

    