from random import randint
import time
mode=['Neil','Juan']
computer=mode[randint(0,1)]
pembahasan=[
    'Poin1 = Ambil contoh untuk di analisis, Identifikasi factor eksternal yang terjadi Identifikasi capabilitas internal organisasi bisnis',
    'Poin 3= 3. peluang  yang ada Tetapkan CSF  & KPI terkait strategi yang anda usulkan'
    ]
bahas=pembahasan[randint(0,1)]
gacha=(input("Mau Gacha Brader? (Yes/No?)"))
if gacha=="yes":
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Congrats Kepada:")
    print(computer,bahas)

