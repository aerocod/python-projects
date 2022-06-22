import string
import random

print("Welcome To Password Generator Program")

Length=int(input("Please Input The Length Of The Password In Number: "))

Symbol=string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase+string.digits

Gabung=random.sample(Symbol,Length)

HasilPassword=''.join(Gabung)

print(HasilPassword)