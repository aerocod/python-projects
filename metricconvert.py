print("Welcome to Metric unit converter")
print("Please Select The Unit: ")
print("1. Km")
print("2. Hm")
print("3. Dam")
print("4. M")
print("5. Dm")
print("6. Cm")
print("7. Mm")
metric=input("Please Select Unit By Number: ")

if metric=='1':
    print("Please Select Unit To Convert")
    print("1. Km To Hm")
    print("2. Km To Dam")
    print("3. Km To M")
    print("4. Km To Dm")
    print("5. Km To Cm")
    print("6. Km to Mm")
    unit=input("Please Select Unit By Number: ")
    if unit=='1':
        km=float(input("Please Input Km: "))
        hm=km*10
        print("Km To Hm: "+str(hm))
        
    elif unit=='2':
        km=float(input("Please Input Km: "))
        dam=km*100
        print("Km To Dam: "+str(dam))
        
    elif unit=='3':
        km=float(input("Please Input Km: "))
        m=km*1000
        print("Km To M: "+str(m))
        
    elif unit=='4':
        km=float(input("Please Input Km: "))
        dm=km*10000
        print("Km To dm: "+str(dm))
        
    elif unit=='5':
        km=float(input("Please Input Km: "))
        cm=km*100000
        print("Km To cm: "+str(cm))
        
    elif unit=='6':
        km=float(input("Please Input Km: "))
        mm=km*1000000
        print("Km To mm: "+str(mm))
        
    else:
        print("Invalid Input")           
                
elif metric=='2':
    print("Please Select Unit To Convert")
    print("1. Hm To Km")
    print("2. Hm To Dam")
    print("3. Hm To M")
    print("4. Hm To Dm")
    print("5. Hm To Cm")
    print("6. Hm to Mm")
    unit=input("Please Select Unit By Number: ")
    if unit=='1':
        Hm=float(input("Please Input Hm: "))
        Km=Hm/10
        print("Hm To Km: "+str(Km))
        
    elif unit=='2':
        Hm=float(input("Please Input Hm: "))
        Dam=Hm*10
        print("Hm To Dam: "+str(Dam))
    
    elif unit=='3':
        Hm=float(input("Please Input Hm: "))
        M=Hm*100
        print("Hm To M: "+str(M))
        
    elif unit=='4':
        Hm=float(input("Please Input Hm: "))
        Dm=Hm*1000
        print("Hm To Dm: "+str(Dm))
        
    elif unit=='5':
        Hm=float(input("Please Input Hm: "))
        Cm=Hm*10000
        print("Hm To Cm: "+str(Cm))
        
    elif unit=='6':
        Hm=float(input("Please Input Hm: "))
        Mm=Hm*100000
        print("Hm To Mm: "+str(Mm))
        
    else:
        print("Invalid Input")
    
elif metric=='3':
    print("Please Select Unit To Convert")
    print("1. Dam To Km")
    print("2. Dam To Hm")
    print("3. Dam To M")
    print("4. Dam To Dm")
    print("5. Dam To Cm")
    print("6. Dam to Mm")
    unit=input("Please Select Unit By Number: ")
    if unit=='1':
        DAm=float(input("Please Input Dam: "))
        KM=DAm/100
        print("Dam To Km: "+str(KM))
        
    elif unit=='2':
        DAm=float(input("Please Input Dam: "))
        HM=DAm/10
        print("Dam To Hm: "+str(HM))
        
    elif unit=='3':
        DAm=float(input("Please Input Dam: "))
        met=DAm*10
        print("Dam To m: "+str(met))
        
    elif unit=='4':
        DAm=float(input("Please Input Dam: "))
        Des=DAm*100
        print("Dam To Dm: "+str(Des))
        
    elif unit=='5':
        DAm=float(input("Please Input Dam: "))
        CM=DAm*1000
        print("Dam To Cm: "+str(CM))
        
    elif unit=='6':
        DAm=float(input("Please Input Dam: "))
        MM=DAm*10000
        print("Dam To Mm: "+str(MM))
        
    else:
        print("Invalid Input")
    
elif metric=='4':
    print("Please Select Unit To Convert")
    print("1. M To Km")
    print("2. M To Hm")
    print("3. M To Dam")
    print("4. M To Dm")
    print("5. M To Cm")
    print("6. M to Mm")
    unit=input("Please Select Unit By Number: ")
    if unit=='1':
        Meter=float(input("Please Input M: "))
        kilo=Meter/1000
        print("M To Km: "+str(kilo))
        
    elif unit=='2':
        Meter=float(input("Please Input M: "))
        Hek=Meter/100
        print("M To Hm: "+str(Hek))
        
    elif unit=='3':
        Meter=float(input("Please Input M: "))
        Dal=Meter/10
        print("M To Dam: "+str(Dal))
        
    elif unit=='4':
        Meter=float(input("Please Input M: "))
        Desi=Meter*10
        print("M To Dm: "+str(Desi))
        
    elif unit=='5':
        Meter=float(input("Please Input M: "))
        Cen=Meter*100
        print("M To Cm: "+str(Cen))
        
    elif unit=='6':
        Meter=float(input("Please Input M: "))
        Mil=Meter*1000
        print("M To Mm: "+str(Mil))
        
    else:
        print("Invalid Input")
    
elif metric=='5':
    print("Please Select Unit To Convert")
    print("1. Dm To Km")
    print("2. Dm To Hm")
    print("3. Dm To Dam")
    print("4. Dm To m")
    print("5. Dm To Cm")
    print("6. Dm to Mm")
    unit=input("Please Select Unit By Number: ")
    if unit=='1':
        Deem=float(input("Please Input Dm: "))
        kaem=Deem/10000
        print("Dm To Km: "+str(kaem))
        
    elif unit=='2':
        Deem=float(input("Please Input Dm: "))
        Haem=Deem/1000
        print("Dm To Hm: "+str(Haem))
        
    elif unit=='3':
        Deem=float(input("Please Input Dm: "))
        Damn=Deem/100
        print("Dm To Dam: "+str(Damn))
        
    elif unit=='4':
        Deem=float(input("Please Input Dm: "))
        Mob=Deem/10
        print("Dm To M: "+str(Mob))
        
    elif unit=='5':
        Deem=float(input("Please Input Dm: "))
        Centi=Deem*10
        print("Dm To Cm: "+str(Centi))
        
    elif unit=='6':
        Deem=float(input("Please Input Dm: "))
        HMily=Deem*100
        print("Dm To Hm: "+str(HMily))
        
    else:
        print("Invalid Input")
    
elif metric=='6':
    print("Please Select Unit To Convert")
    print("1. Cm To Km")
    print("2. Cm To Hm")
    print("3. Cm To Dam")
    print("4. Cm To m")
    print("5. Cm To Dm")
    print("6. Cm to Mm")
    unit=input("Please Select Unit By Number: ")
    if unit=='1':
        Ceem=float(input("Please Input Cm: "))
        Kaaem=Ceem/100000
        print("Cm To Km: "+str(Kaaem))
        
    elif unit=='2':
        Ceem=float(input("Please Input Cm: "))
        hhm=Ceem/10000
        print("Cm To Hm: "+str(hhm))
        
    elif unit=='3':
        Ceem=float(input("Please Input Cm: "))
        dhm=Ceem/1000
        print("Cm To Dam: "+str(dhm))
        
    elif unit=='4':
        Ceem=float(input("Please Input Cm: "))
        mhm=Ceem/100
        print("Cm To m: "+str(mhm))
        
    elif unit=='5':
        Ceem=float(input("Please Input Cm: "))
        dehm=Ceem/10
        print("Cm To dm: "+str(dehm))
        
    elif unit=='6':
        Ceem=float(input("Please Input Cm: "))
        mmhm=Ceem*10
        print("Cm To mm: "+str(mmhm))
        
    else:
        print("Invalid Input")
    
elif metric=='7':
    print("Please Select Unit To Convert")
    print("1. Mm To Km")
    print("2. Mm To Hm")
    print("3. Mm To Dam")
    print("4. Mm To m")
    print("5. Mm To Dm")
    print("6. Mm to Cm")
    unit=input("Please Select Unit By Number: ")
    if unit=='1':
        emem=float(input("Please Input MM: "))
        Keym=emem/1000000
        print("MM To Km: "+str(Keym))
        
    elif unit=='2':
        emem=float(input("Please Input Mm: "))
        haam=emem/100000
        print("Mm To Hm: "+str(haam))
        
    elif unit=='3':
        emem=float(input("Please Input Mm: "))
        daam=emem/10000
        print("Mm To dam: "+str(daam))
        
    elif unit=='4':
        emem=float(input("Please Input Mm: "))
        mmmm=emem/1000
        print("Mm To m: "+str(mmmm))
        
    elif unit=='5':
        emem=float(input("Please Input Mm: "))
        desm=emem/100
        print("Mm To dm: "+str(desm))
        
    elif unit=='6':
        emem=float(input("Please Input Mm: "))
        cmmm=emem/10
        print("Mm To cm: "+str(cmmm))
        
    else:
        print("Invalid Input")
    
else:
    print("Invalid Input")