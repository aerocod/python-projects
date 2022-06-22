print("Welcome To Neil Converter Program Km/h to Mp/h")

print("Silahkan memilih Km/h-MP/H atau MP/H-KM/H")
converter=input("KmToMp or MpToKm: ")

if converter=="KmToMp":
    Km=int(input("Masukan Satuan Kilometer: "))
    KmToMp=(Km*0.6214)
    print("Satuan Km Anda ke Mp adalah: "+str(KmToMp))

elif converter=="MpToKm":
    Mp=int(input("Masukan Satuan Mil: "))
    MpToKm=(Mp*1.6093)
    print("Satuan Mp anda ke Km adalah: "+str(MpToKm))

else:
    print("Cobalah Untuk Memasukan Converter dengan Benar")
    print("Apabila ada Kendala, Mohon Hubungi Neil")