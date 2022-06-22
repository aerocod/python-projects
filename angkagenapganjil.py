while True:
    angka=eval(input("Masukan Angka Untuk Menunjukan Genap/Ganjil: "))
    if angka%2==0:
        print("Angka",angka,"Merupakan Angka Genap")
    elif angka%1==0:
        print("Angka",angka,"Merupakan Angka Ganjil")
    else:
        print("Invalid Input")
        
    again=input("Ingin Memasukan Angka Lagi: (Y/N)?")
    if again=='Y':
        continue
    elif again=='N':
        print("Terima Kasih Sudah Menggunakan Programku")
        break
    else:
        print("Invalid Input")
        break
    