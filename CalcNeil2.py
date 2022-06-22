print("Welcome To Neil's Calculator")
print("                                                ")
print("Terdapat Operasi Yang Tersedia:")
print("+")
print("Tanda '+' Untuk Menambah")
print("-")
print("Tanda '-' untuk Mengurangi")
print("x")
print("Tanda 'x' Untuk Perkalian")
print(":")
print("Tanda ':' untuk Pembagian")
print("                                             ")
operator=input("Masukan operasi:")

while True:
    if operator=='+':
        num1=float(input("Masukan Angka Pertama: "))
        num2=float(input("Masukan Angka Kedua: "))
        plus=(num1+num2)
        print("Hasil Pertambahan Anda: "+str(plus))

    elif operator=='-':
        num1=float(input("Masukan Angka Pertama: "))
        num2=float(input("Masukan Angka Kedua: "))
        minus=(num1-num2)
        print("Hasil Pegurangan Anda: "+str(minus))
        
    elif operator=='x':
        num1=float(input("Masukan Angka Pertama: "))
        num2=float(input("Masukan Angka Kedua: "))
        times=(num1*num2)
        print("Hasil Perkalian Anda: "+str(times))
    
    elif operator==':':
        num1=float(input("Masukan Angka Pertama: "))
        num2=float(input("Masukan Angka Kedua: "))
        divide=(num1/num2)
        print("Hasil Pembagian Anda: "+str(divide))
        
    else:
        print("Invalid Input")
    
    
    