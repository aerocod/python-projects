print("WElcome To KDA(Kill, Death, Assist) Calculator")
print("Welcome To KDA Calculator")
print("Please Select The Calculator: ")
print("1. KDA Calculator")
print("2. KD Calculator")
kdc=input("Please Select The Calculator: ")
if kdc=='1':
    k=int(input("Please Input Kill: "))
    D=int(input("Please Input Death: "))
    A=int(input("Please Input Assist: "))
    ka=k+A
    kd=D+1
    kda=ka/kd
    print("Overall KDA: "+str(kda))  

elif kdc=='2':
    k=int(input("Please Input Kill: "))
    d=int(input("Please Input Death: "))
    kd=k/d
    print("Overall KD: "+str(kd))
    
else: 
    print("Invalid Input")