import random

word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
# Choose a random word from the word_list

guess = input("Guess a letter\n").lower()

for letter in range(0, len(chosen_word)):
    if guess == chosen_word[letter]:
        print("Yes")
    else:
        print("No")
        
display = []
for letter in range(0, len(chosen_word)):
    display.append("_")


for position in range(0, len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        
        print(display)
        
        
        
# Test