while True:
    try:
        print("                                                     ")
        print("Welcome To Rate's Calc")
        print("                                                     ")
        num1=float(input("Please Input Number: "))
        print("                                                     ")
        num2=float(input("Please Input Second Number: "))
        print("                                                     ")
        rate=num1+num2
        rates=rate/2
        print("                                                     ")
        print("Rate Of Number Is: "+str(rates))
        print("                                                     ")
        print("Wanna Rate Some Number Again?")
        print("                                                     ")
        print("1. Yes")
        print("                                                     ")
        print("2. No")
        print("                                                     ")
        again=input("Please Choose Yes/No Using Number: ")
        print("                                                     ")
        if again=='1':
            num1=float(input("Please Input Number: "))
            print("                                                     ")
            num2=float(input("Please Input Second Number: "))
            print("                                                     ")
            rate=num1+num2
            rates=rate/2
            print("Rate Of Number Is: "+str(rates))
            
        elif again=='2':
            print("                                                     ")
            print("Thanks For Using My Rates Calculator")
            break
            
        else:
            print("                                                     ")
            print("Please Input NUMBER, Either Integer or Decimal :D")
    
    except:
        print("                                                     ")
        print("PLEASE INPUT NUMBER, Either Integer Or Decimal :D")