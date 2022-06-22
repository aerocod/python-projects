import math
print("Welcome To Basic Formula")
print("Please Select The Formula")
print("1. Triangle")
print("2. Square")
print("3. Rectangle")
print("4. Circle")
print("5. Trapesium")
print("6. Parallelogram/Jajar Genjang")
print("7. Rhombus/belah ketupat")
print("8. Kite/Layang-layang")
formula=input("Input Number Based On Formula You Want: ")

if formula=="1":
    print("Please Select The Extension Formula: ")
    print("1. Luas Segitiga")
    print("2. Keliling Segitiga")
    print("3. Tinggi Segitiga")
    print("4. Alas Segitiga")
    f=input("Input The Formula Extension Number That You Would Choose: ")
    if f=='1':
        Alas=float(input("Masukan Alas: "))
        Tinggi=float(input("Masukan Tinggi: "))
        Luas=0.5*Alas*Tinggi
        print("Luas Segitiga Adalah: "+str(Luas))
    
    elif f=='2':
        Sisi1=float(input("Masukan Sisi Pertama: "))
        Sisi2=float(input("Masukan Sisi Kedua: "))
        Sisi3=float(input("Masukan Sisi Ketiga: "))
        Kel=Sisi1+Sisi2+Sisi3
        print("Keliling Segitiga Adalah: "+str(Kel))
        
    elif f=='3':
        Luass=float(input("Masukan Luas: "))
        Salas=float(input("Masukan Alas: "))
        Tinggis=2*Luass/Salas
        print("Tinggi Segitiga Adalah: "+str(Tinggis)) 
        
    elif f=='4':
        L=float(input("Masukan Luas: "))
        T=float(input("Masukan Tinggi: "))
        A=2*L/T
        print("Alas Segitiga Adalah: "+str(A)) 
        
    else:
        print("Invalid Input")
        
elif formula=='2':
    print("Please Selecet The Formula Ext: ")
    print("1. Luas")
    print("2. Keliling")
    print("3. Sisi")
    print("4. Diagonal")
    s=input("Please Select The Formula Ext Number You Want: ")
    if s=='1':
        s1=float(input("Masukan Sisi Pertama: "))
        s2=float(input("Masukan Sisi Kedua: "))
        l1=s1*s2
        print("Luas Persegi: "+str(l1))
        
    elif s=='2':
        ss=float(input("Masukan Sisi: "))
        kll=4*ss
        print("Keliling Persegi: "+str(kll))
        
    elif s=='3':
        print("1. Apabila Yang Diketahui Luas")
        print("2. Apabila Yang Diketahui Keliling")
        s4=input("Please Select The Ext Formula Number: ")
        if s4=="1":
            ll=float(input("Masukan Luas: "))
            akar=math.sqrt(ll)
            print("Sisi Persegi: "+str(akar))
        
        elif s4=='2':
            klll=float(input("Masukan Keliling: "))
            skll=klll/4
            print("Sisi Persegi: "+str(skll))
            
    elif s=='4':
        s22=float(input("Masukan Sisi: "))
        d=2*s22*s22
        dia=math.sqrt(d)
        print("Diagonal Persegi: "+str(dia))
        
elif formula=='3':
    print("Please Select The Formula Ext: ")
    print("1. Luas")
    print("2. Keliling")
    print("3. Panjang")
    print("4. Lebar")
    print("5. Diagonal")
    anj=input("Please Select The Formula Ext Num: ")
    if anj=='1':
        pe=flopat(input("Masukan Panjang: "))
        el=float(input("Masukan Lebar: "))
        luaz=pe*el
        print("Luas Persegi Panjang: "+str(luaz))
        
    elif anj=='2':
        pe=flopat(input("Masukan Panjang: "))
        el=float(input("Masukan Lebar: "))
        kel=pe+el
        keli=2*kel
        print("Keliling Persegi Panjang: "+str(keli))
        
    elif anj=='3':
        print("1. Yang Diketahui Luas dan Lebar")
        print("2. Yang Diketahui Keliling dan Lebar")
        zz=input("Input The Formula Ext Num: ")
        if zz=='1':
            asu=float(input("Masukan Luas: "))
            pesu=float(input("Masukan Lebar: "))
            pjg1=asu/pesu
            print("Panjang Persegi Panjang: "+str(pjg1))
            
        elif zz=='2':
            kol=float(input("Masukan Keliling: "))
            lae=float(input("Masukan Lebar: "))
            tol=kol/2
            mea=tol-lae
            print("Panjang Persegi Panjang: "+str(mea))
            
    elif anj=='4':
        print("Please Select formula Ext: ")
        print("1. Yang Diketahui Luas dan Panjang")
        print("2. Yang Diketahui Keliling dan Panjang")
        pukx=input("Please Select The Formula Ext Num: ")
        if pukx=='1':
            mrk=float(input("Masukan Luas: "))
            panj=float(input("Masukan Panjang: "))
            mrpan=mrk/panj
            print("Lebar Persegi Panjang: "+str(mrpan))
            
        elif pukx=='2':
            ua=float(input("Masukan Keliling: "))
            pasx=float(input("Masukan Panjang: "))
            asw=ua/2
            asu=asw-pasx
            print("Lebar Persegi Panjang: "+str(asu))
            
    elif anj=='5':
        uuu=float(input("Masukan Panjang: "))
        aaa=float(input("Masukan Lebar: "))
        ppp=uuu*uuu
        ddd=aaa*aaa
        ooo=ppp+ddd
        diagonal=math.sqrt(ooo)
        print("Diagonal Persegi Panjang: "+str(diagonal))

elif formula=='4':
    print("Please Choose The Extension Formula:")
    print("1. Luas Lingkaran")
    print("2. Keliling Lingkaran")
    print("3. Diameter Lingkaran")
    knt=input("Masukan Nomor Formula Ext: ")
    if knt=='1':
        er=float(input("Masukan Jari-Jari Pertama: "))
        r=float(input("Masukan Jari-Jari Kedua: "))
        Ll=22/7*er*r
        print("Luas Lingkaran: "+str(Ll))
        
    elif knt=='2':
        re=float(input("Masukan Jari-Jari: "))
        Kell=2*22/7*re
        print("Keliling Lingkaran: "+str(Kell))
        
    elif knt=='3':
        ree=float(input("Masukan Jari-Jari: "))
        diam=2*ree
        print("Diameter Lingkaran: "+str(diam))
        
elif formula=='5':
    print("Please Select The Formula Ext")
    print("1. Luas")
    print("2. Keliling")
    print("3. Tinggi")
    print("4. Sisi A atau AB")
    print("5. Sisi B Atau CD")
    print("6. Sisi C atau AD")
    print("7. Sisi D atau BC")
    meks=input("Please Select The Formula Ext Number: ")
    if meks=='1':
        sisi1=float(input("Masukan Sisi Sejajar Pertama: "))
        sisi2=float(input("Masukan Sisi Sejajar Kedua: "))
        tinggi=float(input("Masukan Tinggi: "))
        luast=sisi1+sisi2
        luastra=luast*0.5*tinggi
        print("Luas Trapesium Adalah: "+str(luastra))
        
    elif meks=='2':
        Ab=float(input("Masukan Sisi AB"))
        Bc=float(input("Masukan Sisi BC"))
        Cd=float(input("Masukan Sisi CD"))
        Da=float(input("Masukan Sisi Da"))
        kelt=Ab+Bc+Cd+Da
        print("Keliling Trapesium Adalah: "+str(kelt))
        
    elif meks=='3':
        luass=float(input("Masukan Luas: "))
        sisi1=float(input("Masukan Sisi Sejajar Pertama: "))
        sisi2=float(input("Masukan Sisi Sejajar Kedua: "))
        ting=2*luass
        gint=sisi1+sisi2
        tinggii=ting/gint
        print("Tinggi Trapesium Adalah: "+str(tinggii))
        
    elif meks=='4':
        print("Please Select The Formula Ext")
        print("1. Yang Diketahui Luas Dan Tinggi")
        print("2. Yang Diketahui Keliling")
        konst=input("Please Select The Formula Ext Num:")
        if konst=='1':
            L=float(input("Masukan Luas: "))
            T=float(input("Masukan Tinggi: "))
            B=float(input("Masukan Sisi B"))
            dual=2*L
            pual=dual/T
            bual=pual-B
            print("Sisi A Adalah: "+str(bual))
            
        elif konst=='2':
            kll=float(input("Masukan Keliling: "))
            Cd=float(input("Masukan Sisi CD: "))
            Bc=float(input("Masukan Sisi BC: "))
            Ad=float(input("Masukan Sisi AD:  "))
            kel=kll-Cd-Bc-Ad
            print("Sisi A Adalah: "+str(kel))
            
    elif meks=='5':
        print("Please Select The Formula Ext")
        print("1. Yang Diketahui Luas Dan Tinggi")
        print("2. Yang Diketahui Keliling") 
        kontsa=input("Please Input The Formula Ext: ")
        if kontsa=='1':
            L=float(input("Masukan Luas: "))
            T=float(input("Masukan Tinggi: "))
            A=float(input("Masukan Sisi A"))
            dual=2*L
            pual=dual/T
            bual=pual-A
            print("Sisi B Adalah: "+str(bual))
            
        elif kontsa=='2':
            kll=float(input("Masukan Keliling: "))
            Cd=float(input("Masukan Sisi AB: "))
            Bc=float(input("Masukan Sisi BC: "))
            Ad=float(input("Masukan Sisi AD: "))
            kel=kll-Cd-Bc-Ad
            print("Sisi A Adalah: "+str(kel))
        
    elif meks=='6':
        kll=float(input("Masukan Keliling: "))
        Cd=float(input("Masukan Sisi CD: "))
        Bc=float(input("Masukan Sisi BC: "))
        Ad=float(input("Masukan Sisi AB: "))
        kel=kll-Cd-Bc-Ad
        print("Sisi AD Adalah: "+str(kel))
        
    elif meks=='7':
        kll=float(input("Masukan Keliling: "))
        Cd=float(input("Masukan Sisi CD: "))
        Bc=float(input("Masukan Sisi AD: "))
        Ad=float(input("Masukan Sisi AB: "))
        kel=kll-Cd-Bc-Ad
        print("Sisi BC Adalah: "+str(kel))
        
elif formula=="6":
    print("Please Select The Formula Ext")
    print("1. Luas Jajar Genjang")
    print('2. Alas Jajar Genjang')
    print('3. Tinggi Jajar Genjang')
    mwk=input("Please Select The Formula Ext Num: ")
    if mwk=='1':
        alas=float(input("Masukan Alas: "))
        tinggi=float(input("Masukan Tinggi: "))
        luas=alas*tinggi
        print("Luas Jajar Genjang Adalah: "+str(luas))
        
    elif mwk=='2':
        lua=float(input("Masukan Luas: "))
        ting=float(input("Masukan Tinggi: "))
        al=lua/ting
        print("Alas Jajar Genjang Adalah: "+str(al))
        
    elif mwk=='3':
        lua=float(input("Masukan Luas: "))
        ala=float(input("Masukan Alas: "))
        tinggg=lua/ala
        print("Tinggi Jajar Genjang Adalah: "+str(tinggg))
        
elif formula=='7':
    print("Please Select The Formula Ext")
    print("1. Keliling Belah Ketupat")
    print("2. Luas Belah Ketupat")
    print("3. Sisi Belah Ketupat")
    print("4. Diagonal 1 Belah Ketupat")
    print("5. Diagonal 2 Belah Ketupat")
    mlbb=input("Please Select The Formula Ext Num: ")
    if mlbb=='1':
        print("Jika Sisi Sama, Masukan Sisi Yang Sama Seterusnya")
        s=float(input("Masukan Sisi Pertama: "))
        ss=float(input("Masukan Sisi Kedua: "))
        sss=float(input("Masukan Sisi Ketiga: "))
        ssss=float(input("Masukan Sisi Keempat: "))
        luas=s+ss+sss+ssss
        print("Keliling Belah Ketupat Adalah: "+str(luas))
        
    elif mlbb=='2':
        d1=float(input("Masukan Diagonal 1: "))
        d2=float(input("Masukan Diagonal 2: "))
        lll=0.5*d1*d2
        print("Luas Belah Ketupat Adalah: "+str(lll))
        
    elif mlbb=='3':
        kll=float(input("Masukan Keliling"))
        kl4=kll/4
        print("Sisi Belah Ketupat Adalah: "+str(kl4))
        
    elif mlbb=='4':
        l=float(input("Masukan Luas: "))
        dd=float(input("Masukan D2: "))
        diag1=2*l/dd
        print("Diagonal 1 Adalah: "+str(diag1))
        
    elif mlbb=='5':
        el=float(input("Masukan Luas: "))
        de=float(input("Masukan D1: "))
        diag2=2*el/de
        print("Diagonal 2 Adalah: "+str(diag2))
        
elif formula=='8':
    print("Please Select The Formula Ext")
    print("1. Luas")
    print("2. Keliling")
    print("3. Diagonal 1")
    print("4. Diagonal 2")
    print("5. A Atau B")
    print("6. C Atau D")
    mkc=input("Please Select The Formula Ext: ")
    if mkc=='1':
        d1=float(input("Masukan Diagonal 1: "))
        d2=float(input("Masukan Diagonal 2: "))
        lll=0.5*d1*d2
        print("Luas Layang Layang Adalah: "+str(lll))
        
    elif mkc=='2':
        print("Please Select The Formula Ext")
        print("1. Dik a b c d")
        print("2. Dik A C")
        pl=input("Please Select The Formula Ext: ")
        if pl=='1':
            s=float(input("Masukan Sisi Pertama: "))
            ss=float(input("Masukan Sisi Kedua: "))
            sss=float(input("Masukan Sisi Ketiga: "))
            ssss=float(input("Masukan Sisi Keempat: "))
            luas=s+ss+sss+ssss
            print("Keliling Layang Layang Adalah: "+str(luas))
            
        elif pl=='2':
            a=float(input("Masukan Sisi A: "))
            c=float(input("Masukan Sisi C:"))
            ac=a+c
            kel=2*ac
            print("Keliling Layang Layang Adalah: "+str(kel))
            
    elif mkc=='3':
        l=float(input("Masukan Luas: "))
        dd=float(input("Masukan D2: "))
        diag1=2*l/dd
        print("Diagonal 1 Adalah: "+str(diag1))
        
    elif mkc=='4':
        el=float(input("Masukan Luas: "))
        de=float(input("Masukan D1: "))
        diag2=2*el/de
        print("Diagonal 2 Adalah: "+str(diag2))
        
    elif mkc=='5':
        kell=float(input("Masukan Keliling: "))
        ce=float(input("Masukan Sisi C: "))
        setk=0.5*kell
        aorb=setk-ce
        print(" Sisi A Atau B Adalah: "+str(aorb))
        
    elif mkc=='6':
        keli=float(input("Masukan Keliling: "))
        ha=float(input("Masukan Sisi A: "))
        setke=0.5*keli
        cord=setke-ha
        print("Sisi C Atau D Adalah: "+str(cord))
         
else:
    print("Invalid Input")