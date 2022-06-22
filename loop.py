def bikin_kalimat(kata,banyak_kata):
    kalimat=kata*banyak_kata
    return kalimat

while True:
    kata=input("Masukan Kata: "" ")
    banyak_kata=int(input("Masukan Banyak Kata: "))
    print("Hasil Kata: ",bikin_kalimat(kata,banyak_kata))

    again=input("Mau Membuat Kata Lagi? (yes/no?) ")
    if again=="no" or again=='No':
        print("Thanks For Using My Program")
        break
    elif again=='yes' or again=='Yes':
        continue
    else:
        print("Invalid Input, Thanks For Using My Program")
        break
        