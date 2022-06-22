print("Selamat Datang di Cm To Inch and Inch To Cm Calculator")
print("                                                         ")
print("Silahkan Pilih Operasi")
print("1. Cm To Inch")
print("2. Inch To Cm")
print("Harap masukan Nomor dari operasi yang ingin di pilih")

converter=input("Masukan Nomor Operasi Yang Diinginkan: ")
if converter==("1"):
    Km=float(input("Harap Masukan Satuan Cm: "))
    Inch=Km*0.393701
    print("Satuan Cm Anda Ke Inch= "+str(Inch))
    
elif converter==("2"):
    Inches=float(input("Harap Masukan Satuan Inch: "))
    Itk=Inches*2.54
    print("Satuan Inch Anda Ke Cm= "+str(Itk))
    
else:
    print("Invalid Input")