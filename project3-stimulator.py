import random


while True :
    print(random.randint(1,6))
    roll=input("you want to roll the dice again [y/n] : ")
    if roll.lower()=='y':
        continue
    else:
        break 


