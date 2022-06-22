while True:
    nilai=eval(input("Masukan Nilai: "))
    
    if nilai >=90 and nilai <100:
        print("Grade A")
        
    elif nilai >=80 and nilai <90:
        print('Grade B')
    
    elif nilai >=70 and nilai <80:
        print('Grade C')
        
    elif nilai >=60 and nilai <70:
        print('Grade D')
    
    elif nilai <60:
        print('Grade E')
    break
    