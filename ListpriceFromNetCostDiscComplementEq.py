while True:
    print("Cari List Price Dari Net Cost Dan Trade Discount (Complement)")
    print("                ")
    com1=float(input("Masukan Trade Discount Complement 1: "))
    print("                ")
    com2=float(input("Masukan Trade Discount Complement 2: "))
    print("                ")
    com3=float(input("Masukan Trade Discount Complement 3: "))
    complement=com1*com2*com3

    netcost=float(input("Masukan Netcost: "))

    listprice=netcost/complement
    print("                ")
    print("List Price Dari Komplement dan Net Price Adalah: ",listprice)
    break