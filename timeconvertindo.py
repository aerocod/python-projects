print("Welcome To Time Converter")
print("Please Select The Time: ")
print("1. Known Time=WIB")
print("2. Known Time=WITA")
print("3. Know Time=WIT")
print("For '24.00' Please Use '00.00'")
time=input("Please Input The Known Time By Number: ")

if time=='1':
    Wib=eval(input("Masukan Jam WIB Nya, Contoh '3.00': "))
    if Wib==23.00:
        print("WITA= 00.00")
        print("WIT= 01.00")
        
    elif Wib==22.00:
        print("WITA= 23.00")
        print("WIT= 00.00")
        
    else:
        Wita=Wib+1.00
        Wit=Wib+2.00
        print("WITA= "+str(Wita))
        print("WIT= "+str(Wit))
        
elif time=='2':
    wita=eval(input("Masukan Jam WITA Nya, Contoh '3.00': "))
    if wita==23.00:
        print("WIB= 22.00")
        print("WIT= 00.00")
        
    else:
        weibe=wita-1.00
        weite=wita+1.00
        print("WIB= "+str(weibe))
        print("WIT= "+str(weite))

elif time=='3':
    wit=eval(input("Masukan Jam WIT Nya, Contoh '3.00': "))
    if wit==2.00:
        print("WIB= 00.00")
        print("WITA= 01.00")
        
    elif wit==1.00:
        print("WIB= 23.00")
        print("WITA= 00.00")
        
    else:
        ewieb=wit-2.00
        weitee=wit-1.00
        print("WIB= "+str(ewieb))
        print("WITA= "+str(weitee))
        

