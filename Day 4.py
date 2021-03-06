import random

# random_integer = random.randint(100,200)
# print(random_integer)




# Heads or tails
userGuess = input("Hello. Lets play heads or tails. Guess Heads or Tails.\n")

coin = random.randint(0,1)

if coin == 0:
    headsOrTails = "heads"
else:
    headsOrTails = "tails"
    
if userGuess.lower() == headsOrTails.lower():
    print(f"You are correct! The coin landed on {headsOrTails}!")
else:
    print(f"Nope. You suck at guessing. It landed on {headsOrTails}.")