import random

Player1= input('Select ROCK , PAPER or SCISSOR : ').upper()
Player2=random.choice(['ROCK','PAPER','SCISSOR']).upper()
print("player2 selected ", Player2)

if Player1=="rock" and Player2=="paper":
    print("Player2 won")
elif Player1=="paper" and Player2=="scissor":
    print("Player2 won")
elif Player1=="scissor" and Player2=="rock":
    print("Player2 won")
elif Player1==Player2:
    print("tie")
else:
    print("player1 won")


