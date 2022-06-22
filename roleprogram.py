print("Welcome To Role Program")
print("Nama Available Are:")
print("1. Neil")
print("2. John")
print("3. Henry")
nama=input("Choose The Available Name by Number: ")
if nama=='1':
    print("1. Today Neil Is Sweeping")
    print("2. Today Neil Is Throw Trash")
    print("3. Today Neil Is Sweeping Table")
    hari=input("Please Select The Statement Num Above: ")
    if hari=='1':
        print("Today John Is Throw Trash")
        print("Today Henry Is Sweeping Table")
        
    elif hari=='2':
        print("Today John Is Sweeping Table")
        print("Today Henry Is Sweeping ")
        
    elif hari=='3':
        print("Today John Is Sweeping")
        print("Today Henry Is Throw Trash")
        
    else:
        print("Invalid Input")
        
elif hari=='2':
    print("1. Today John Is Sweeping")
    print("2. Today John Is Throw Trash")
    print("3. Today John Is Sweeping Table")
    hari=input("Please Select The Statement Num Above: ")
    if hari=='1':
        print("Today Neil Is Throw Trash")
        print("Today Henry Is Sweeping Table")
        
    elif hari=='2':
        print("Today Neil Is Sweeping Table")
        print("Today Henry Is Sweeping ")
        
    elif hari=='3':
        print("Today Neil Is Sweeping")
        print("Today Henry Is Throw Trash")
        
    else:
        print("Invalid Input")
    
elif hari=='3':
    print("1. Today Henry Is Sweeping")
    print("2. Today Henry Is Throw Trash")
    print("3. Today Henry Is Sweeping Table")
    hari=input("Please Select The Statement Num Above: ")
    if hari=='1':
        print("Today John Is Throw Trash")
        print("Today Neil Is Sweeping Table")
        
    elif hari=='2':
        print("Today John Is Sweeping Table")
        print("Today Neil Is Sweeping ")
        
    elif hari=='3':
        print("Today John Is Sweeping")
        print("Today Neil Is Throw Trash")
        
    else:
        print("Invalid Input")
        
else:
    print("Invalid Input")
