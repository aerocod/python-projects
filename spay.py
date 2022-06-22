print("Welcome To Henry Mart")
print("Please Select The Item Below: ")
print("1. Drinks")
print("2. Foods")
item=input("Please Select The Item By Number: ")
if item=='1':
    print("Please Select The Drinks Below: ")
    print("1. Milky Boba Ori 25k")
    print("2. Milky Boba Brown Sugar 30k")
    drink=input("Please Choose The Drinks By Number: ")
    if drink=='1':
        print("The Total is 25000 Rupiah")
        print("Do You Want Some Food Too? ")
        f2d=input("Yes/No: ")
        if f2d=='Yes':
            print("1. Indomie With Salted Egg 15k")
            print("2. Cheese Burger With Egg 25K")
            fod=input("Please Select The Food Above By Number: ")
            if fod=='1':
                print("The Total Is 40000 Rupiah")
                pay=int(input("Please Pay The Bill: "))
                if pay <=39999:
                    print("You Dont Have Enough Money To Pay The Bill")
                    
                elif pay==40000:
                    print("Your Money Is Enoguh, Please Take Our Beverage At Jln.Sempak Kuda No. 69")
                    
                elif pay >=40000:
                    Change=pay-40000
                    print("Please Take Our Beverage At Jln.Sempak Kuda No. 69, Here's Your Change: "+str(Change))
                    
                else:
                    print("Invalid Input")
                    
            elif fod=='2':
                print("The Total Is 50000 Rupiah")
                pay=int(input("Please Pay The Bill: "))
                if pay <=49999:
                    print("You Dont Have Enough Money To Pay The Bill")
                    
                elif pay==50000:
                    print("Your Money Is Enoguh, Please Take Our Beverage At Jln.Sempak Kuda No. 69")
                    
                elif pay >=50000:
                    Cange=pay-50000
                    print("Please Take Our Beverage At Jln.Sempak Kuda No. 69, Here's Your Change: "+str(Cange))
                    
                else:
                    print("Invalid Input")
                
        elif f2d=='No':
            print("The Total Is 25000 Rupiah")
            pay=int(input("Please Pay The Bill: "))
            if pay <=24999:
                print("You Dont Have Enough Money To Pay The Bill")
                    
            elif pay==25000:
                print("Your Money Is Enoguh, Please Take Our Beverage At Jln.Sempak Kuda No. 69")
                    
            elif pay >=25000:
                Chnge=pay-25000
                print("Please Take Our Beverage At Jln.Sempak Kuda No. 69, Here's Your Change: "+str(Chnge))
                    
            else:
                print("Invalid Input")
                
    elif drink=='2':
        print("The Total is 30000 Rupiah")
        print("Do You Want Some Food Too? ")
        f2d=input("Yes/No: ")
        if f2d=='Yes':
            print("1. Indomie With Salted Egg 15k")
            print("2. Cheese Burger With Egg 25K")
            fod=input("Please Select The Food Above By Number: ")
            if fod=='1':
                print("The Total Is 45000 Rupiah")
                pay=int(input("Please Pay The Bill: "))
                if pay <=44999:
                    print("You Dont Have Enough Money To Pay The Bill")
                    
                elif pay==45000:
                    print("Your Money Is Enoguh, Please Take Our Beverage At Jln.Sempak Kuda No. 69")
                    
                elif pay >=45000:
                    Change=pay-45000
                    print("Please Take Our Beverage At Jln.Sempak Kuda No. 69, Here's Your Change: "+str(Change))
                    
                else:
                    print("Invalid Input")
                    
            elif fod=='2':
                print("The Total Is 55000 Rupiah")
                pay=int(input("Please Pay The Bill: "))
                if pay <=54999:
                    print("You Dont Have Enough Money To Pay The Bill")
                    
                elif pay==55000:
                    print("Your Money Is Enoguh, Please Take Our Beverage At Jln.Sempak Kuda No. 69")
                    
                elif pay >=55000:
                    Cange=pay-55000
                    print("Please Take Our Beverage At Jln.Sempak Kuda No. 69, Here's Your Change: "+str(Cange))
                    
                else:
                    print("Invalid Input")
                
        elif f2d=='No':
            print("The Total Is 30000 Rupiah")
            pay=int(input("Please Pay The Bill: "))
            if pay <=29999:
                print("You Dont Have Enough Money To Pay The Bill")
                    
            elif pay==30000:
                print("Your Money Is Enough, Please Take Our Beverage At Jln.Sempak Kuda No. 69")
                    
            elif pay >=30000:
                Chne=pay-30000
                print("Please Take Our Beverage At Jln.Sempak Kuda No. 69, Here's Your Change: "+str(Chne))
                    
            else:
                print("Invalid Input")
                
elif item=='2':
    print("Please Select The Food Below")
    print("1. Indomie With Salted Egg 15k")
    print("2. Cheese Burger With Egg 25K")
    drink=input("Please Choose The Foods By Number: ")
    if drink=='1':
        print("The Total is 15000 Rupiah")
        print("Do You Want Some Drinks Too? ")
        f2d=input("Yes/No: ")
        if f2d=='Yes':
            print("Please Select The Drinks Below: ")
            print("1. Milky Boba Ori 25k")
            print("2. Milky Boba Brown Sugar 30k")
            fod=input("Please Select The Drinks Above By Number: ")
            if fod=='1':
                print("The Total Is 40000 Rupiah")
                pay=int(input("Please Pay The Bill: "))
                if pay <=39999:
                    print("You Dont Have Enough Money To Pay The Bill")
                    
                elif pay==40000:
                    print("Your Money Is Enoguh, Please Take Our Beverage At Jln.Sempak Kuda No. 69")
                    
                elif pay >=40000:
                    Change=pay-40000
                    print("Please Take Our Beverage At Jln.Sempak Kuda No. 69, Here's Your Change: "+str(Change))
                    
                else:
                    print("Invalid Input")
                    
            elif fod=='2':
                print("The Total Is 45000 Rupiah")
                pay=int(input("Please Pay The Bill: "))
                if pay <=44999:
                    print("You Dont Have Enough Money To Pay The Bill")
                    
                elif pay==45000:
                    print("Your Money Is Enoguh, Please Take Our Beverage At Jln.Sempak Kuda No. 69")
                    
                elif pay >=45000:
                    Cange=pay-45000
                    print("Please Take Our Beverage At Jln.Sempak Kuda No. 69, Here's Your Change: "+str(Cange))
                    
                else:
                    print("Invalid Input")
                
        elif f2d=='No':
            print("The Total Is 15000 Rupiah")
            pay=int(input("Please Pay The Bill: "))
            if pay <=14999:
                print("You Dont Have Enough Money To Pay The Bill")
                    
            elif pay==15000:
                print("Your Money Is Enoguh, Please Take Our Beverage At Jln.Sempak Kuda No. 69")
                    
            elif pay >=15000:
                Chnge=pay-15000
                print("Please Take Our Beverage At Jln.Sempak Kuda No. 69, Here's Your Change: "+str(Chnge))
                    
            else:
                print("Invalid Input")
                
    elif drink=='2':
        print("The Total is 25000 Rupiah")
        print("Do You Want Some Drinks Too? ")
        f2d=input("Yes/No: ")
        if f2d=='Yes':
            print("Please Select The Drinks Below: ")
            print("1. Milky Boba Ori 25k")
            print("2. Milky Boba Brown Sugar 30k")
            fod=input("Please Select The Drinks Above By Number: ")
            if fod=='1':
                print("The Total Is 50000 Rupiah")
                pay=int(input("Please Pay The Bill: "))
                if pay <=49999:
                    print("You Dont Have Enough Money To Pay The Bill")
                    
                elif pay==50000:
                    print("Your Money Is Enoguh, Please Take Our Beverage At Jln.Sempak Kuda No. 69")
                    
                elif pay >=50000:
                    Change=pay-50000
                    print("Please Take Our Beverage At Jln.Sempak Kuda No. 69, Here's Your Change: "+str(Change))
                    
                else:
                    print("Invalid Input")
                    
            elif fod=='2':
                print("The Total Is 55000 Rupiah")
                pay=int(input("Please Pay The Bill: "))
                if pay <=54999:
                    print("You Dont Have Enough Money To Pay The Bill")
                    
                elif pay==55000:
                    print("Your Money Is Enoguh, Please Take Our Beverage At Jln.Sempak Kuda No. 69")
                    
                elif pay >=55000:
                    Cange=pay-55000
                    print("Please Take Our Beverage At Jln.Sempak Kuda No. 69, Here's Your Change: "+str(Cange))
                    
                else:
                    print("Invalid Input")
                
        elif f2d=='No':
            print("The Total Is 25000 Rupiah")
            pay=int(input("Please Pay The Bill: "))
            if pay <=24999:
                print("You Dont Have Enough Money To Pay The Bill")
                    
            elif pay==25000:
                print("Your Money Is Enough, Please Take Our Beverage At Jln.Sempak Kuda No. 69")
                    
            elif pay >=25000:
                Chne=pay-25000
                print("Please Take Our Beverage At Jln.Sempak Kuda No. 69, Here's Your Change: "+str(Chne))
                    
            else:
                print("Invalid Input")
    
else:
    print("Invalid Input")
