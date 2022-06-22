import math
print("Welcome To Math Quardatic Equation Solver")
a=float(input("Please Input a Koeficient: "))
b=float(input("Please Input b Koeficient: "))
c=float(input("Please Input c Koeficient: "))  
d=b*b
foura=4*a*c
dfour=d-foura
db=math.sqrt(dfour)
xmin=-b-db
xpos=-b+db
aa=2*a
x1=xmin/aa
x2=xpos/aa
print("Result Can Be: ",x1,"And",x2)
    
