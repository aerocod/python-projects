print("Welcome To Calories Calculator")
print("Please Select Your Gender")
print("1. Male")
print("2. Female")
g=input("Please Select Your Gender By Number: ")

if g=='1':
    w=float(input("Please Input Your Weight In Kg: "))
    h=float(input("Please Input Your Height in Cm: "))
    a=int(input("Please Input Your Age: "))
    bmr=10*w+6.25*h-5*a+5
    mwl=bmr*0.9
    wl=bmr*0.79
    ewl=bmr*0.59
    print("Your Daily Calories is: "+str(bmr),"Calories")
    print("If You Wanna Weight Loss: ")
    print("Mild Weight Loss: "+str(mwl),"Calories")
    print("Weight Loss: "+str(wl),"Calories")
    print("Extreme Weight Loss: "+str(ewl),"Calories")
    
elif g=='2':
    w=float(input("Please Input Your Weight In Kg: "))
    h=float(input("Please Input Your Height in Cm: "))
    a=int(input("Please Input Your Age: "))
    bmr=10*w+6.25*h-5*a+5
    mwl=bmr*0.89
    wl=bmr*0.77
    ewl=bmr*0.54
    print("Your Daily Calories is: "+str(bmr),"Calories")
    print("If You Wanna Weight Loss: ")
    print("Mild Weight Loss: "+str(mwl),"Calories")
    print("Weight Loss: "+str(wl),"Calories")
    print("Extreme Weight Loss: "+str(ewl),"Calories")
    