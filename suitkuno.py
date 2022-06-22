from random import randint

mode=['Gajah','Semut','Orang']
computer=mode[randint(0,2)]
player = False
print("Selamat Datang Di Game Suit Jadul")    
print("Masing-masing Player Diharapkan Masukan Keyword Antara lain; (Gajah,Semut,Orang)")
print("Cara Bermain Sangat Mudah")

while player==False:
    nama=input("Siapa Nama Kamu? ")
    bot=input("Siapa Nama Lawan Kamu, sesuai Keinginan? ")
    print("Silahkan Pilih Mode: ")
    player=input("Gajah,Semut,Orang? ")
    if player==computer:
        print("Hasilnya Seri")
    elif player=='Gajah' or player=='gajah':
        if computer=='Semut':
            print("Selamat",bot,"Menang, Semut Berhasil Menewaskan Gajah",nama)
        else:
            print("Selamat",nama,"Menang, Gajah Berhasil Menewaskan Orang",bot)
    elif player=="Semut" or player=='semut':
        if computer=='Orang':
            print("Selamat",bot,"Menang, Orang Berhasil Menewaskan Semut",nama)
        else:
            print("Selamat",nama,"Menang, Semut Berhasil Menewaskan Gajah",bot)
    elif player=='Orang' or player=="orang":
        if computer=='Gajah':
            print("Selamat",bot,"Menang, Gajah Berhasil Menewaskan Orang",nama)
        else:
            print("Selamat",nama,"Menang, Orang Berhasil Menewaskan Semut",bot)
    else:
        print("Harap Masukan Keyword Yang Benar (Gajah/Semut/Orang)")
        
    player=False
    computer=mode[randint(0,2)]
    
    again=input("Ingin Bermain Lagi? (Yes/No): ")
    if again=='yes' or again=='Yes':
        continue
    else:
        print("Terima Kasih Sudah Bermain :D")
        break