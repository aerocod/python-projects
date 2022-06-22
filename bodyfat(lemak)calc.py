print("Welcome To Body Fat Calculator")
print("If You Want Exit The Program, Please Type 'Exit'")
while True:
    print("Please Select Units By Number Given Below: ")
    print("1. Metric Units (Cm And M)")
    print("2. Us Units (inch And Lb)")
    unit=input("Please Select The Unit By Number: ")
    if unit=='1':
        try:
            mass=float(input("Please Input Your Weight By Kg: "))
            height=float(input("Please Input Height In Meter: "))
            height2=height*height
            bmi=mass/height2
            print("BMI Results= ",bmi)
            print("1. Adult Males(18+)")
            print("2. Adult Females(18+)")
            print("3. Boys (0-17)")
            print("4. Girls (0-17)")
            age=input("Please Input Your Category By Number Given Above: ")
            if age=='1':
                umur=int(input("Please Input Your Exact Age: "))
                if umur <=17:
                    print("Invalid Input")
                    break
                bfp=1.2*bmi
                bfpa=0.23*umur
                bfppa=bfp+bfpa-16.2
                print("Body Fat Percentage: ",bfppa)
            elif age=='2':
                umur=int(input("Please Input Your Exact Age: "))
                if umur <=17:
                    print("Invalid Input")
                    break
                bfp=1.2*bmi
                bfpa=0.23*umur
                bfppa=bfp+bfpa-5.4
                print("Body Fat Percentage: ",bfppa)
            elif age=='3':
                umur=int(input("Please Input Your Exact Age: "))
                if umur >=17:
                    print("Invalid Input")
                    break
                bfp=1.51*bmi
                bfpa=0.70*umur
                bfppa=bfp-bfpa-2.2
                print("Body Fat Percentage: ",bfppa)
            elif age=='4':
                umur=int(input("Please Input Your Exact Age: "))
                if umur >=17:
                    print("Invalid Input")
                    break
                bfp=1.51*bmi
                bfpa=0.70*umur
                bfppa=bfp-bfpa+1.4
                print("Body Fat Percentage: ",bfppa)
            else:
                print("Invalid Input")
                break    
        except:
            print("Invalid Input")
            print("Please Reset The Calculator")
            break
    elif unit=='2':
        try:
            mass=float(input("Please Input Your Weight By Lbs: "))
            height=float(input("Please Input Height In inch: "))
            height2=height*height
            bmi=703*mass/height*height
            print("BMI Results= ",bmi)
            print("1. Adult Males(18+)")
            print("2. Adult Females(18+)")
            print("3. Boys (0-17)")
            print("4. Girls (0-17)")
            age=input("Please Input Your Category By Number Given Above: ")
            if age=='1':
                umur=int(input("Please Input Your Exact Age: "))
                if umur <=17:
                    print("Invalid Input")
                    break
                bfp=1.2*bmi
                bfpa=0.23*umur
                bfppa=bfp+bfpa-16.2
                print("Body Fat Percentage: ",bfppa)
            elif age=='2':
                umur=int(input("Please Input Your Exact Age: "))
                if umur <=17:
                    print("Invalid Input")
                    break
                bfp=1.2*bmi
                bfpa=0.23*umur
                bfppa=bfp+bfpa-5.4
                print("Body Fat Percentage: ",bfppa)
            elif age=='3':
                umur=int(input("Please Input Your Exact Age: "))
                if umur >=17:
                    print("Invalid Input")
                    break
                bfp=1.51*bmi
                bfpa=0.70*umur
                bfppa=bfp-bfpa-2.2
                print("Body Fat Percentage: ",bfppa)
            elif age=='4':
                umur=int(input("Please Input Your Exact Age: "))
                if umur >=17:
                    print("Invalid Input")
                    break
                bfp=1.51*bmi
                bfpa=0.70*umur
                bfppa=bfp-bfpa+1.4
                print("Body Fat Percentage: ",bfppa)
            else:
                print("Invalid Input")
                break    
        except:
            print("Invalid Input")
            print("Please Reset The Calculator")
            break
    else:
        print("Invalid Input")
        break
        