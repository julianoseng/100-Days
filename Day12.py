#Scope
# #Scope

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies() 
# print(f"enemies outside function: {enemies}"





#Number Guessing Game
"""
    Guess a number between 1 and 100. Easy has 10 attempts. Hard has 5 attempts.
    If the number you guess is higher than the secret number, print "too high", and vice versa.
    Print welcome, im thinking of a number between 1 and 100, ask user to choose difficulty.
"""

import random
# random int and assign it to secret number variable
attempts_left = 0
game_over = False

secret_number = random.randint(1,100)

print("Welcome to the number guessing game!")
difficulty = input("Choose a difficulty. Either 'easy' or 'hard': ")
user_guess = int(input("I am thinking of a number between 1 and 100. Guess a number: "))

if difficulty == 'easy':
    attempts_left = 10
elif difficulty == 'hard':
    attempts_left = 5

def number_guessing():
    global user_guess
    user_guess = int(input("Guess another number : "))

def number_guessing_game():
    global game_over
    global attempts_left
    global secret_number
    
    while game_over == False:
        if user_guess == secret_number:
            game_over = True
            print(f"Congrats, you got it! {secret_number} was the number I was looking for!")
        elif user_guess > secret_number:
            print("Too high. Try again!")
            attempts_left -= 1
        elif user_guess < secret_number:
            print("Too low. Try again! ")
            attempts_left -= 1
        
        if attempts_left != 0:
            number_guessing()
        elif attempts_left == 0:
            game_over = True
            print(f"You suck. The number was {secret_number}.")
            
number_guessing_game()


enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")