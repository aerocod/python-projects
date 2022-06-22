print("Series Discount Calculator")
print("                                        ")

print("Please Choose Discount Mode Series Calculator")
print("1. 2 Series Discount")
print("2. 3 Series Discount")

mode=int(input("Please Choose Mode: "))

while True:
    
    if mode==1:
        print("Anda Diharapkan Memasukan 2 Diskon")
        price=float(input("Masukan Harga: "))
        print("                              ")
        disc1=float(input("Masukan Diskon Ke 1: "))
        print("                                   ")
        
        firstd=disc1/100
        
        diskon1=price*firstd
        print("Diskon pertama ialah: ",diskon1)
        print("                                       ")
        disc2=float(input("Masukan Diskon Ke 2: "))
        print("                                           ")
        secd=disc2/100
        
        diskon2=diskon1*secd
        
        finaldisc=price-(diskon1+diskon2)
        print("Harga Setelah Chain Discount ",disc1,"%"," dan ",disc2,"%"," = ",finaldisc)
        
    elif mode==2:
        print("Anda Diharapkan Memasukan 3 Diskon")
        price=float(input("Masukan Harga: "))
        print("                              ")
        disc1=float(input("Masukan Diskon Ke 1: "))
        print("                                   ")
        
        firstd=disc1/100
        
        diskon1=price*firstd
        print("                                       ")
        
        disc2=float(input("Masukan Diskon Ke 2: "))
        print("                                           ")
        secd=disc2/100
        
        diskon2=diskon1*secd
        
        disc3=float(input("Masukan Diskon Ke 3: "))
        print("                                      ")
        
        thirdd=disc3/100
        
        diskon3=diskon2*thirdd
        print("Diskon 1= ",diskon1)
        print("Diskon 2= ",diskon2)
        print("Diskon 3= ",diskon3)
        totaldisc=diskon1+diskon2+diskon3
        finaldisc=price-totaldisc
        print("                                 ")
        print("Harga",price,"Setelah Chain Discount ",disc1,"%"," dan ",disc2,"%"," dan ",disc3,"%", "=",finaldisc)
        
        print("Mau Calc Lagi? (y/n)")
        again=input("Masukan Keyword: ")
        if again=="y":
            continue
        else:
            break