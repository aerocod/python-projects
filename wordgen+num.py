import random
import string

password=int(input("Len Of Words By Num: "))
Symbol=string.ascii_letters+string.digits

Gabung=random.sample(Symbol,password)

HasilPassword=''.join(Gabung)

print(HasilPassword)
