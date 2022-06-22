from random import randint
import time
angka=[0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

player2= angka[randint(0,30)]

player=False
print("--------------------------------------")
print("Welcome To BJ Program")
print("BJ Program Definition: ")
print("                                          ")
time.sleep(2)
print("There Are Block Counted as 0")
print("There Are Seed Counted as 0")
print("                                          ")
time.sleep(2)
print("There are Int Numbers From 0-21")
print("21 Is The Highest And Can Also Called as Jackpot")
print("                                          ")
time.sleep(2)
print("The Range Number Is Between 0-21")
print("Conclusion: The Higher The Number You Win")
print("                                          ")
time.sleep(2)
print("If Those Int Number >21 Will Count As Lose or Jebs a.k.a Jebol")
print("Can Be Played For 1 Round Only :D")
print("Please Enjoy This Bj :D")
print("                                          ")
print("--------------------------------------")
while player==False:
    name=input("What's Your Name? ")
    print("                                          ")
    name2=input("Whats Your Rival Name? ")
    print("                                          ")
    print("Alright Lets Gooooooooooooo")
    print("                                          ")
    print("Please Press '1' To Start The Gacha")
    print("                                          ")
    gacha=input("Please Input '1' To Start Gacha: ")
    
    if gacha=='1':
        player=angka[randint(0,30)]
        if player==player2:
            print("Your Gacha Numbers Is Tie With Score: ",name,player,"And",name2,player2)
        
        elif player==0:
            if player2>=0 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
                
            elif player2>=21:
                print("Results Tie: ",name2,player2, "As Tie As", name,player)
                
        elif player2==0:
            if player>=0 and player<=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
            elif player>=21:
                print("Results Tie: ",name2,player2, "As Tie As", name,player)
        
        elif player==1:
            if player2>=1 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=1:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
        
        elif player==2:
            if player2>=2 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=2:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==3:
            if player2>=3 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=3:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==4:
            if player2>=4 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=4:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==5:
            if player2>=5 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=5:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
        
        elif player==6:
            if player2>=6 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=6:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==7:
            if player2>=7 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=7:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==8:
            if player2>=8 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=8:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==9:
            if player2>=9 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=9:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==10:
            if player2>=10 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=10:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==11:
            if player2>=11 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=11:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==12:
            if player2>=12 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=12:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==13:
            if player2>=13 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=13:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==14:
            if player2>=14 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=14:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==15:
            if player2>=15 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=15:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==16:
            if player2>=16 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=16:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==17:
            if player2>=17 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=17:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==18:
            if player2>=18 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=18:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
        
        elif player==19:
            if player2>=19 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=19:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==20:
            if player2>=20 and player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2<=20:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==21:
            if player2<=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
            elif player2>=21:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==22:
            if player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2>=22:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==23:
            if player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2==22:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2>=23:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==24:
            if player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2>=22 and player2<=23:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2>=24:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==25:
            if player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2>=22 and player2<=24:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2>=25:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==26:
            if player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2>=22 and player2<=25:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2>=26:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==27:
            if player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2>=22 and player2<=26:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2>=27:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==28:
            if player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2>=22 and player2<=27:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2>=28:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==29:
            if player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2>=22 and player2<=28:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2>=29:
                print("Congrats: ",name,player, "Beats", name2,player2)
                
        elif player==30:
            if player2<=21:
                print("Congrats: ",name2,player2, "Beats", name,player)
            elif player2>=22 and player2<=29:
                print("Congrats: ",name2,player2, "Beats", name,player)
    
    else:
        print("Please Input The Right Keyword :D")
        
    player=False
    player2=angka[randint(0,30)]
    print("                                          ")
    again=input("Wanna Play Again? (Please Input Yes/No): ")
    if again=="Yes" or again=="yes":
        continue
    else:
        print("Thanks For Playing This Game :D")
        break