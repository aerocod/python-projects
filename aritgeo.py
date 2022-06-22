import math

print("Welcome To Geometery And Aritmethic Calculator")
print("Please Select The Calculator Menu")
print("1. Aritmethic Calculator")
print("2. Geometry Calculator")

while True:
    print("1. Aritmethic Calculator")
    print("2. Geometry Calculator")
    calc=input("Please Input The Calculator Mode Ny Number: ")
    if calc=='1':
        print("1. Line Aritmethic Calculator")
        print("2. Row Aritmethic Calculator")
        acalc=input("Please Select Calculator Mode By Number: ")
        if acalc=='1':
            print("1. Regular Formula")
            print("2. Middle Variable Formula")
            lform=input("Please Input Formula By Number: ")
            if lform=='1':
                a=float(input("Input, Please Input The First tribe(a): "))
                b=float(input("Please Input b (u2-u1): "))
                n=int(input("Please Input Total Tribe: "))
                
                formula=n-1
                formulanb=formula*b
                rformula=formulanb+a
                print("U",n,"=",rformula)
                
            elif lform=='2':
                a=float(input("Please Input The First Tribe (u1) or (a): "))
                un=int(input("Please Input Un: "))
                
                u=a+un
                ut=u/2
                print("UT (Middle Tribe Is): ",ut)
                
            else:
                print('Please Input The Valid Number')
                break
            
        elif acalc=='2':
            print("1. Formula That 'Un' Is Known")
            print("2. Formula That N and B are Known")
            lform=input("Please Input Formula By Number: ")
            if lform=='1':
                a=float(input("Input, Please Input The Tribe Knwon(n): "))
                b=float(input("Please Input un : "))
                n=int(input("Please Input 'S' Tribe: "))
                
                formula=1+b
                formulanb=a/2
                rformula=formulanb*formula
                print("S",n,"=",rformula)
                
            elif lform=='2':
                a=float(input("Please Input The First Tribe (u1) or (a): "))
                un=int(input("Please Input b: "))
                n=int(input("Please Input n: "))
                
                n2=n/2
                a2=2*a+n-1
                ut=n2+a2*un
                print("Sn (Row Aritmethic Is): ",ut)
            else:
                print('Please Input The Valid Number')
                break
            
        else:
            print("Please Input Number Correctly")
            break
        
    elif calc=='2':
        print("1. Line Geometry Calculator")
        print("2. Row Geometry Calculator")
        gcalc=input("Please Input Formula By Number: ")
        if gcalc=='1':
            print("1. Line Geometry Calculator")
            print("2. Middle Tribe Geometry")
            geocalc=input("Please Input Formula By Number: ")
            if geocalc=='1':
                a=float(input("Please Input a or u1: "))
                r=float(input("Please Input rasio: "))
                n=float(input("Please Input n: "))
                
                un=n-1
                un1=r**un
                untotal=a*un1
                print("U",n,"=",untotal)
            elif geocalc=='2':
                u1=float(input("Please Input u1 or a: "))
                un=float(input("Please Input Un: "))
                
                unu1=u1-un
                ut=math.sqrt(unu1)
                print("Middle Tribe Is: ",ut)
            else:
                print("Please Input Number Correctly")
            break
        
        elif gcalc=='2':
            print("1. If r Are more than 1 (>1)")
            print("2. If 1>r")
            form=input("Please Input Formula by Number: ")
            if form=='1':
                a=float(input("Please Input a: "))
                r=float(input("Please Input r: "))
                n=float(input("Please Input n: "))
                
                rn=r**n
                b=1-r
                rn1=1-rn
                arn=a*rn1
                arnslash=arn/b
                print("Geometery Row, Sn=",arnslash)
                
            elif form=='2':
                a=float(input("Please Input a: "))
                r=float(input("Please Input r: "))
                n=float(input("Please Input n: "))
                
                rn=r**n
                b=r-1
                rn1=rn-1
                arn=a*rn1
                arnslash=arn/b
                print("Geometery Row, Sn=",arnslash)
            else:
                print("Please Input The Number Correctly")
                break
                
    else:
        print("Please Input The Number Correctly")
        break