# rock paper scissor
import random

Player=input("enter the play : ")
computer=random.choice(['rock','paper','scissor'])
print(computer)

if Player == 'rock' and computer== 'paper' :
    print("This rounds winner is Computer ")
elif Player == 'scissor' and computer== 'rock'  :
    print("This rounds winner is Computer ")
elif Player == 'paper' and computer== 'scissor' :
    print("This rounds winner is Computer ")
elif Player == computer :
    print("its a draw")
else:
    print("This rounds winner is Player ")