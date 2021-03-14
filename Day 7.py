import random
import hangman_art
import hangman_words


# Choose a random word from the word_list.
chosen_word = random.choice(hangman_words.word_list)
lives = 6
guesses = 0
letters_already_guessed = []

#Prints out an underscore in place of all letters in the word.
display = []
letterAmount = 0
for letter in range(0, len(chosen_word)):
    display.append("_")
    letterAmount += 1


#Welcome
print(hangman_art.logo)

print(f"The word you are trying to guess has {letterAmount} letters in it.\n\n")

print("----------------------------------------------------------------------\n\n")

def hang_man_guess():
    global lives
    global guesses
    global letters_already_guessed
    
    if guesses == 0:
        guess = input("Guess a letter.\n").lower()
    elif guesses > 0:
        print("\nLetters already guessed:")
        print(letters_already_guessed)
        print("\n")
        print(display)
        guess = input("\nGuess another letter.\n").lower()
    letters_already_guessed.append(guess)
    #Takes input and inserts it into the display list, in the proper position, if the letter is in the word.
    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter    
            guesses += 1
            print(f"{guess} is a letter in this word.")  
    
    #Subtracts lives if the guessed letter is not in the word.
    if guess not in chosen_word:
        lives -= 1
        guesses += 1
        if lives == 1:
            print(f"\n{guess} is not in this word. You have {lives} chance left.")
        else:
            print(f"\n{guess} is not in this word. You have {lives} chances left.")

    if lives == 6:
        print(hangman_art.stages[6])
    elif lives == 5:
        print(hangman_art.stages[5])
    elif lives == 4:
        print(hangman_art.stages[4])
    elif lives == 3:
        print(hangman_art.stages[3])
    elif lives == 2:
        print(hangman_art.stages[2])
    elif lives == 1:
        print(hangman_art.stages[1])
    elif lives == 0:
        print(hangman_art.stages[0])
    
# Turns display list into a string.
def display_to_string(display):
    str1 = ""
    for letter in display:
        str1 += letter
    return str1


#Checks for win or lose.
def check_win_lose():
    if display_to_string(display) == chosen_word:
        print(f"\nYou win!!!! {chosen_word} was the word!")
    elif lives == 0:
        print(f"\nYou lose. The word was {chosen_word}!!!!")


#Game engine while loop.
while lives != 0 and display_to_string(display) != chosen_word:
    hang_man_guess()
else:    
    check_win_lose()
    input()