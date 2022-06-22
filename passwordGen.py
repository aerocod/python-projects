import random
import string

print("Welcome To Password Generator")

panjang=int(input("Masukan Panjanag Password Yang Diinginkan: "))

Simbol=string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

acakPass= random.sample(Simbol,panjang)

HasilPassword= ''.join(acakPass)

print(HasilPassword)