from random import randint

mode=[2]
computer=mode[randint(0)]

player = False
print("Selamat Datang Di Game Sumpit MultiPlayer")    
print("Masing-masing Player Akan mendapat 2 sumpit/jari Di awal Game")
print("Cara Bermain Sangat Mudah")

while player==False:
    nama=input("Siapa Nama Kamu? ")
    bot=input("Siapa Nama Lawan Kamu, sesuai Keinginan? ")
    print("Masukan Kata Sandi 'Mulai', untuk Bermian")
    player=input("Masukan Sandi: ")
    if player=='mulai':
        if player==2 and computer==2:
            print("Silahkan Pilih Mode Serang: ")
            print("1. Gabungkan Jari Kiri dan Kanan (2)Sumpit Setelah Digabung")
            print("2. Attack Salah 1 Jari Lawan, (Lawan Memperoleh 1 Jari Tambahan)")
            player=input("Silahkan Pilih Mode, Sesuai Nomor: ")
            
            if player=='1':
                print("Sekarang giliran Lawan: ")
                print("Silahkan Pilih Mode Serang: ")
                print("1. Gabungkan Jari Kiri dan Kanan (3)Jari")
                print("2. Serang Lawan Menggunakan 2 Jari Sekaligus")
                print("3. Serang Lawan Menggunakan 1 Jari")
                computer=input("Masukan Mode Serang Sesuai Nomor: ")
                
    