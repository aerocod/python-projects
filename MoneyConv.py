print("welcome to money converter")
print("1. Rupiah(Indonesia)")

money=input("Please Select The Money To Convert: ")
if money=='1':
    print("Please Select Currency")
    print("1. US Dollar (USA)")
    print("2. Ringgit (Malaysia)")
    convert=input("Please Select The Conveert By Number: ")
    if convert=='1':
        rupiah=float(input("Please Input The Rupiah: "))
        USD=rupiah/14000
        print("Rupiah To USD= "+str(USD))
        
    elif convert=='2':
        rupiah=float(input("Please Input The Rupiah: "))
        ringgit=rupiah/3000
        print("Rupiah To Ringgit= "+str(ringgit))
        
    else:
        print("Invalid Input")
        
else:
    print("Invalid Input")