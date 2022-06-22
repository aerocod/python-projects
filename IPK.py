print("Selamat Datang di IPK Calculator")
while True:
    ip=float(input("Masukan Ip semester 1, Contoh : 3.69: " ))
    if ip >=4.01:
        print("Invalid Input")
    
    elif ip <=4.00:
        print("                                            ")
    
    else:    
        print("Invalid Input")
    ip2=float(input("Masukan Ip Semester 2: "))
    if ip2 >=4.01:
        print("Invalid Input")
    
    elif ip2 <=4.00:
        print("                                            ")
    
    else:
        print("Invalid Input")
    ip3=float(input("Masukan Ip Semester 3: "))
    if ip3 >=4.01:
        print("Invalid Input")
    
    elif ip3 <=4.00:
        print("                                            ")
    
    else:
        print("Invalid Input")
    ip4=float(input("Masukan Ip Semester 4: "))
    if ip4 >=4.01:
        print("Invalid Input")
    
    elif ip4 <=4.00:
        print("                                            ")
    
    else:
        print("Invalid Input")
    ip5=float(input("Masukan Ip Semester 5: "))
    if ip5 >=4.01:
        print("Invalid Input")
    
    elif ip5 <=4.00:
        print("                                            ")
    
    else:
        print("Invalid Input")
    ip6=float(input("Masukan Ip Semester 6: "))
    if ip6 >=4.01:
        print("Invalid Input")
    
    elif ip6 <=4.00:
        print("                                            ")
    
    else:
        print("Invalid Input")
    ip7=float(input("Masukan Ip Semester 7: "))
    if ip7 >=4.01:
        print("Invalid Input")
    
    elif ip7 <=4.00:
        print("                                            ")

    else:
        print("Invalid Input")
    ip8=float(input("Masukan Ip Semester 8: "))
    if ip8 >=4.01:
        print("Invalid Input")

    elif ip8 <=4.00:
        print("                                            ")

    else:
        print("Invalid Input")
    
    ipk=ip+ip2+ip3+ip4+ip5+ip6+ip7+ip8
    ipku=ipk/8
    if ipku >=4.01:
        print("Invalid Input")
    
    elif ipku <=4.00:
        print("                                            ")
    
    else:
       print("Invalid Input")
    
    break
print("Hasil IPK Anda Adalah: "+str(ipku),"IPK")