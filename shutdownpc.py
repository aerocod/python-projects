import os
  
shutdown=(input("Shutdown Comp: (Yes/No"))
if (shutdown=='Yes'):
    os.system("shutdown /s /t 3")
else:
    print("Computer Wont Shutdown Unless You Typer Yes")
