# import random

# random_integer = random.randint(100,200)
# print(random_integer)




# Heads or tails
# import random
# userGuess = input("Hello. Lets play heads or tails. Guess Heads or Tails.\n")

# coin = random.randint(0,1)

# if coin == 0:
#     headsOrTails = "heads"
# else:
#     headsOrTails = "tails"
    
# if userGuess.lower() == headsOrTails.lower():
#     print(f"You are correct! The coin landed on {headsOrTails}!")
# else:
#     print(f"Nope. You suck at guessing. It landed on {headsOrTails}.")





# Banker Roulette

# import random

# print("Hello! Lets see who has to pay for the entire bill!")

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# randomName = random.randint(0,len(names)-1)

# print(names[randomName] + " has to pay the bill!")




# Treasure Map
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# inputPosition = input("Where do you want to put the treasure? ")

# h1 = int(inputPosition[0])
# v1 = int(inputPosition[1])
# map[h1 -1][v1 - 1] = "x"

# print(f"{row1}\n{row2}\n{row3}")





# Rock Paper Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

playerDecision = input("Lets play rock paper scissors. Choose one.")

# 0 = Rock
# 1 = Paper
# 2 = Scissors
possibleChoice = ["Rock","Paper","Scissors"]
choiceCheck = ["rock","paper","scissors"]
computerRandomDecisionInt = random.randint(0,2)
computerRandomDecision = possibleChoice[computerRandomDecisionInt]



if playerDecision.lower() == "rock" and computerRandomDecisionInt == 2:
    print("Rock beats scissors. You win!")
elif playerDecision.lower() == "paper" and computerRandomDecisionInt == 0:
    print("Paper beats rock. You win!")
elif playerDecision.lower() == "scissors" and computerRandomDecisionInt == 1:
    print("Scissors beats paper. You win!")
elif playerDecision.lower() == computerRandomDecision.lower():
    print("Tie")
else:
    print(f"{computerRandomDecision} beats {playerDecision}. You lose.")





