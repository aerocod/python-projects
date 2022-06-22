from random import randint
mode = ["Batu", "Kertas", "Gunting"]

computer = mode[randint(0,2)]

player = False

while player == False:
    nama=input("Siapa Nama Kamu? ")
    bot=input("Siapa Nama Lawan Kamu (Namakan Sesuai Keinginan)? ")
    print("Silahkan Pilih Mode: ")
    player = input("Batu, Gunting, Kertas? ")
    if player == computer:
        print("Hasil Seri!")
    elif player == "Batu" or player=='batu':
        if computer == "Kertas":
            print("Kamu Kalah", nama, computer, bot, "Dicover", player)
        else:
            print("Kamu Menang", nama, player, "Menghancurkan", computer, bot)
    elif player == "Kertas" or player=='kertas':
        if computer == "Gunting":
            print("Kamu Kalah!", nama, computer, bot, "menggunting", player)
        else:
            print("Kamu menang!", nama, player, "dicover", computer, bot)
    elif player == "Gunting" or player=='gunting':
        if computer == "Batu":
            print("Kamu Kalah...", nama, computer, bot, "menghancurkan", player)
        else:
            print("Kamu menang!", nama, player, "menggunting", computer, bot)
    else:
        print("Mohon masukan keyword yang benar (Batu/Gunting/Kertas)")
        
    player = False
    computer = mode[randint(0,2)]
    
    again=input("Mau Bermain Lagi? (yes/no)?")
    if again=='yes':
        continue
    elif again=='no':
        break
    else:
        print("Invalid Input")
        break