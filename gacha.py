from random import randint
import time
angka=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

computer= angka[randint(0,36)]

player = False
while player== False:
    print("Welcome To Gacha Program")
    print("Normal Gacha Definition: ")
    time.sleep(3)
    print("                                                         ")
    print("There are 0 Until 36 Numbers")
    print("                                                         ")
    print("0 Is The Strongest Among Any Other Numbers")
    print("                                                         ")
    print("If You Get Higher Number Than Your Rival, You Win")
    print("                                                         ")
    print("Else, You Will Lose")
    print("                                                         ")
    print("QQ Gacha Definition: ")
    print("                                                         ")
    print("There Are 0 Until 36 Numbers")
    print("                                                         ")
    print("0 Is The Strongest Among Any Other Numbers")
    print("                                                         ")
    print("In QQ, The The Back/Tail Of The Given Number Will Be The Indicator")
    print("                                                         ")
    print("If The Tail/Back Number That You Get Are Higher Than Your Rival, You Win")
    print("                                                         ")
    print("Else, You Will Lose")
    name=input("What's Your Name? ")
    bot=input("What's Your Rival Name? ")
    player=input("Masukan 'Go' Untuk Memulai gacha: ")
    if player=='Go' or player=='go':
        print("Please Choose The Mode Below: ")
        print("1. Normal Gacha")
        print("2. QQ Gacha")
        gacha=input("Please Input Gacha Above, by Number: ")
        if gacha=='1':
            player= angka[randint(0,36)]
            if player==computer:
                print("Hasil Gacha Seri")
        
            elif player==0:
                if computer>=0:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
            
            elif computer==0:
                if player>=0:
                    print("Selamat",bot,computer,"Berhasil Mengalahkan",name,player)
            
            elif player==1:
                if computer>=1:
                    print("Selamat",bot,computer,"Berhasil Mengalahkan",name,player)
                    
            elif player==2:
                if computer>=2:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=1:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==3:
                if computer>=3:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=3:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==4:
                if computer>=4:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=4:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
            elif player==5:
                if computer>=5:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=5:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player) 
                    
            elif player==6:
                if computer>=6:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=6:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==7:
                if computer>=7:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=7:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==8:
                if computer>=8:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=8:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==9:
                if computer>=9:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=9:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==10:
                if computer>=10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=10:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==11:
                if computer>=11:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=11:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==12:
                if computer>=12:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=12:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==13:
                if computer>=13:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=13:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==14:
                if computer>=14:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=14:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==15:
                if computer>=15:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=15:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==16:
                if computer>=16:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=16:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)      
            
            elif player==17:
                if computer>=17:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=17:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==18:
                if computer>=18:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=18:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==19:
                if computer>=19:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=19:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==20:
                if computer>=20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=20:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)  
            
            elif player==21:
                if computer>=21:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=21:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==22:
                if computer>=22:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=21:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==23:
                if computer>=23:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=23:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==24:
                if computer>=24:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=24:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==25:
                if computer>=25:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=25:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)

            elif player==26:
                if computer>=26:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=26:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==27:
                if computer>=27:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=27:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==28:
                if computer>=28:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=28:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==29:
                if computer>=29:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=29:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==30:
                if computer>=30:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=30:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player) 
            
            elif player==31:
                if computer>=31:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=31:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==32:
                if computer>=32:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=32:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==33:
                if computer>=33:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=33:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==34:
                if computer>=34:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=34:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==35:
                if computer>=35:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=35:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==36:
                if computer>=36:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=36:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
        elif gacha=='2':
            player= angka[randint(0,36)]
            if player==computer:
                print("The Results Is Draw")
        
            elif player==0:
                if computer>=0:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
            
            elif computer==0:
                if player>=0:
                    print("Selamat",bot,computer,"Berhasil Mengalahkan",name,player)
            
            elif player==1:
                if computer>=1:
                    print("Selamat",bot,computer,"Berhasil Mengalahkan",name,player)
                elif computer==31:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==21:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==11:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                    
            elif player==2:
                if computer>=2:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=2:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==22:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==32:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==12:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                    
            elif player==3:
                if computer>=3:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=3:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)  
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==23:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==33:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==13:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                    
            elif player==4:
                if computer>=4:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=4:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==24:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==34:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==14:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)  
                    
            elif player==5:
                if computer>=5:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=5:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player) 
                elif computer==25:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==35:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==15:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                    
            elif player==6:
                if computer>=6:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=6:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==26:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==36:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==16:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                    
            elif player==7:
                if computer>=7:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=7:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==27:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==17:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=31:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)
                    
            elif player==8:
                if computer>=8:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=8:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==28:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==18:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=31:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)
                    
            elif player==9:
                if computer>=9:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=9:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==29:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==19:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=31:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)
                    
            elif player==10:
                if computer==20:
                    print("Hasil",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==30:
                    print("Hasil",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer<=10:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=10:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer>=20:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer>=30:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)
                    
            elif player==11:
                if computer>=11:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=11:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==21:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==31:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==1:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=31:
                    print("Selamat",bot,computer,"Berhasil Mengalahkan",name,player)
                elif computer>=2 and computer <10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                
                    
            elif player==12:
                if computer>=12:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=12:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==22:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==32:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==2:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=32:
                    print("Selamat",bot,computer,"Berhasil Mengalahkan",name,player)
                elif computer>=3 and computer <10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==13:
                if computer>=13:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=13:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==23:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==33:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==3:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=33:
                    print("Selamat",bot,computer,"Berhasil Mengalahkan",name,player)
                elif computer>=4 and computer <10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==14:
                if computer>=14:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=14:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==24:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==34:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==4:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=34:
                    print("Selamat",bot,computer,"Berhasil Mengalahkan",name,player)
                elif computer>=5 and computer <10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==15:
                if computer>=15:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=15:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==25:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==35:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==5:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=35:
                    print("Selamat",bot,computer,"Berhasil Mengalahkan",name,player)
                elif computer>=6 and computer <10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==16:
                if computer>=16:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=16:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==26:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==36:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==6:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=31:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)   
                elif computer>=21:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)
                elif computer>=7 and computer <10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                
            elif player==17:
                if computer>=17:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=17:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==27:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==7:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=31:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)   
                elif computer>=21:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)
                elif computer>=8 and computer <10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==18:
                if computer>=18:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=18:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==28:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==8:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=31:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)   
                elif computer>=21:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)
                elif computer>=9 and computer <10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                    
            elif player==19:
                if computer>=19:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=19:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==29:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==9:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=31:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)   
                elif computer>=21:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)
                    
            elif player==20:
                if computer==10:
                    print("Hasil",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==30:
                    print("Hasil",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer<=10:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=10:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer>=20:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer>=30:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)
                
            
            elif player==21:
                if computer>=21:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=21:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==11:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==31:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==1:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=31:
                    print("Selamat",bot,computer,"Berhasil Mengalahkan",name,player)
                elif computer>=2 and computer<10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=12 and computer<20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)  
                    
            elif player==22:
                if computer>=22:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=21:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==12:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==32:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==2:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=32:
                    print("Selamat",bot,computer,"Berhasil Mengalahkan",name,player)
                elif computer>=3 and computer<10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=13 and computer<20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)  
                    
            elif player==23:
                if computer>=23:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=23:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==13:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==33:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==3:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=33:
                    print("Selamat",bot,computer,"Berhasil Mengalahkan",name,player)
                elif computer>=4 and computer<10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=14 and computer<20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)  
                    
            elif player==24:
                if computer>=24:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=24:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==14:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==34:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==4:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=34:
                    print("Selamat",bot,computer,"Berhasil Mengalahkan",name,player)
                elif computer>=5 and computer<10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=15 and computer<20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)  
                    
            elif player==25:
                if computer>=25:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=25:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==15:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==35:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==5:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=36:
                    print("Selamat",bot,computer,"Berhasil Mengalahkan",name,player)
                elif computer>=6 and computer<10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=16 and computer<20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)  

            elif player==26:
                if computer>=26:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=26:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==16:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==36:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==6:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=31:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)
                elif computer>=7 and computer<10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=17 and computer<20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)  
                    
            elif player==27:
                if computer>=27:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=27:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==17:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==7:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=31:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)
                elif computer>=8 and computer<10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=18 and computer<20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)  
                    
            elif player==28:
                if computer>=28:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=28:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                        print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==18:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==8:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=31:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)
                elif computer>=9 and computer<10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=19 and computer<20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)     
                
            elif player==29:
                if computer>=29:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=29:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==19:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==9:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=31:
                    print("Selamat",bot,computer,"Berhasil Mengalahkan",name,player) 
                    
            elif player==30:
                if computer==20:
                    print("Hasil",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==10:
                    print("Hasil",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer<=10:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=10:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer>=20:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer>=30:
                    print("Selamat",name,player,"Berhasil Mengalahkan",bot,computer)
            
            elif player==31:
                if computer>=31:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=31:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==30:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==11:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==21:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==31:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==1:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=2 and computer<10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=12 and computer<20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)  
                elif computer>=22 and computer<30:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)   

            elif player==32:
                if computer>=32:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=32:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==30:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==12:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==22:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==2:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=3 and computer<10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=13 and computer<20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)  
                elif computer>=23 and computer<30:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)   
                    
            elif player==33:
                if computer>=33:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=33:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==30:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==13:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==23:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==3:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=4 and computer<10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=14 and computer<20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)  
                elif computer>=24 and computer<30:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)   
                    
            elif player==34:
                if computer>=34:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=34:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==30:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==24:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==14:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==4:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=5 and computer<10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=15 and computer<20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)  
                elif computer>=25 and computer<30:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)   
                    
            elif player==35:
                if computer>=35:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=35:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==30:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==15:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==25:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==5:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=6 and computer<10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=16 and computer<20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)  
                elif computer>=26 and computer<30:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)   
                    
            elif player==36:
                if computer>=36:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer<=36:
                    print("Selamat",name,player,"Berhasil Mengalahkan",computer,bot)
                elif computer==0:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==30:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer==16:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==26:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer==6:
                    print("Hasil",name,player,"Seri Terhadap Hasil",bot,computer)
                elif computer>=7 and computer<10:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)
                elif computer>=17 and computer<20:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)  
                elif computer>=27 and computer<30:
                    print("Selamat",computer,bot,"Berhasil Mengalahkan",name,player)   
            
        
        else:
            print("Mohon Masukan Keyword Yang Benar (Go/go)")
            
        player=False
        computer=angka[randint(0,36)]
        
    
    again=input("Wanna Play Again? (Yes/No)")
    if again=='Yes' or again=="yes":
        continue
    else:
        print("Thanks For Using My Program")
        break
    