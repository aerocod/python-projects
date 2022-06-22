print("Welcome To Ideal And Normal Weight Calculator")
print("Input Your Height To Reveal the Weight")

Height=float(input("Input Your Height in Cm: "))
NormalWeight=(Height-100)
IdealWeight=NormalWeight-NormalWeight*1/10
print("Your Normal Weight is: "+str(NormalWeight))
print("Your Ideal Weight is: "+str(IdealWeight))