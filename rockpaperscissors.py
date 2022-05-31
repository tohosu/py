# Rock Paper Scissor Game
import random

# Read input from user
player = input("rock paper scissors (Type r, p, or s): ")
# post: choice has user's input
print(player)

# only allow r, p, or s as valid input
if player == "r" or player == "p" or player == "s":
    print("yes")
else:
    print("wrong")
    
# computer make a choice
choices =["r","p","s"]
comp = random.choice(choices)
# post: comp has computer's choice

# print results
# print player's choice
txt = "You chose "
if (player == "r"):
    txt += "ROCK."
if (player == "p"):
    txt += "PAPER."
if (player == "s"):
    txt += "SCISSOR."
# print computer's choice
txt += " Computer chose "
if (comp == "r"):
    txt += "ROCK."
if (comp == "p"):
    txt += "PAPER."
if (comp == "s"):
    txt += "SCISSOR."
# tie cases
if (player == "r" and comp == "r"):
    txt += " There is a tie"
if (player == "p" and comp == "p"):
    txt += " There is a tie"
if (player == "s" and comp == "s"):
    txt += " There is a tie"
# win/lose cases
if (player == "r" and comp == "p"):
    txt += " Computer wins"
if (player == "r" and comp == "s"):
    txt += " Player wins"
if (player == "p" and comp == "r"):
    txt += " Computer wins"
if (player == "p" and comp == "s"):
    txt += " Player wins"
if (player == "s" and comp == "r"):
    txt += " Computer wins"
if (player == "s" and comp == "p"):
    txt += " Player wins"

print(txt)
