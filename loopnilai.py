while True:
    angka=(int(input("Insert Your Score Between 0-100: ")))
    
    if angka >=101:
        print("Invalid Input")
        print("Please Input Score Given :D")
        break
    
    elif angka <0:
        print("Invalid Input")
        print("Please Input Score Given :D")
        break
    
    elif angka >=85 and angka <101:
        print("You Got A Score")
        print("Try Again And Try Your Best")
        
    elif angka >=70 and angka <85:
        print("You Got B Score")
        print("Try Harder Ang Good Luck")
    
    elif angka >=60 and angka <70:
        print("Yoou Got C Score")
        print("Pretty Good Keep it Up")
    
    elif angka >=40 and angka <60:
        print("You Got D Score")
        print("Awesome, Keep It Up")
    
    elif angka >=0 and angka <40:
        print("You Got E Score")
        print("You Master It, Keep It Up")
        
    else:
        print("Please Input The Valid Number")
        break
    
    again=input("Want To Input Score Again? (Yes/No)?")
    
    if again=='Yes' or again=="yes":
        pass
    
    else:
        print("Thanks For Using My Program :D")
        break
        
        