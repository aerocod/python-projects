while True:
    print("                   ")
    print("Anda Diharapkan Memasukan 2 Diskon")
    print("                   ")
    price=float(input("Masukan Harga: "))
    print("                              ")
    disc1=float(input("Masukan Diskon Ke 1: "))
    print("                                   ")
        
    firstd=disc1/100
        
    diskon1=price*firstd
    
    harga1=price-diskon1
    print("Harga Setelah Diskon 1: ",harga1)
    print("                                       ")
    
    disc2=float(input("Masukan Diskon Ke 2: "))
    print("                                           ")
    secd=disc2/100
        
    diskon2=harga1*secd
        
    harga2=harga1-diskon2
    
    print("Harga ke 2 adalah: ",harga2)
    print("                   ")
    disc3=float(input("Masukan Diskon Ke 3: "))
    print("                      ")
    thirdd=disc3/100
    
    diskon3=harga2*thirdd
    
    harga3=harga2-diskon3
    
    finaldisc=harga3
    print("Harga Setelah Diskon 3: ",harga3)
    print("                   ")
    print("Diskon pertama ialah: ",diskon1)
    print("                   ")
    print("Diskon kedua ialah: ",diskon2)
    print("                   ")
    print("Diskon ketiga ialah: ",diskon3)
    print("                   ")
    print("Harga",price," - (",diskon1," + ",diskon2," + ",diskon3,")", "Setelah Chain Discount ",disc1,"%"," dan ",disc2,"%"," = ",finaldisc)