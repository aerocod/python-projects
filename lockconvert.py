print("Welcome To Growtopia Lock Converter")
print("Please Select The Locks: ")
print("1. World Locks (Wl)")
print("2. Diamond Locks (Dl)")
print("3. Blue Gem Locks (BGL)")
lock=input("Please Select The Lock By The Number Given: ")

if lock=='1':
    wl=int(input("Please Input The Wl: "))
    dl=wl/100
    bgl=wl/10000
    print("Wl to Dl= "+str(dl))
    print("Wl To BGL= "+str(bgl))
    
elif lock=='2':
    dl=int(input("Please Input The DL: "))
    wl=dl*100
    bgl=dl/100
    print("Dl To Wl= "+str(wl))
    print("BGL To Dl= "+str(bgl))
    
elif lock=='3':
    bgl=int(input("Please Input BGL= "))
    wl=bgl*10000
    dl=bgl*100
    print("BGL To Wl= "+str(wl))
    print("BGL To Dl= "+str(dl))
    
else:
    print("Invalid Input")