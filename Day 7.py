import random


# Choose a random word from the word_list.
word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
lives = 6

#Prints out an underscore in place of all letters in the word.
display = []
for letter in range(0, len(chosen_word)):
    display.append("_")


def hang_man_guess():
    global lives
    
    guess = input("Guess a letter\n").lower()
    #Takes input and inserts it into the display list, in the proper position, if the letter is in the word.
    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter    
            print(display)        
    
    #Subtracts lives if the guessed letter is not in the word.
    if guess not in chosen_word:
        print(f"{guess} is not in this word. Try another letter.")
        lives -= 1


# Turns display list into a string.
def display_to_string(display):
    str1 = ""
    for letter in display:
        str1 += letter
    return str1


#Checks for win or lose.
def check_win_lose():
    if display_to_string(display) == chosen_word:
        print("You win!")
    elif lives == 0:
        print("You lose.")


#Game engine while loop.
while lives != 0 and display_to_string(display) != chosen_word:
    hang_man_guess()
else:    
    check_win_lose()