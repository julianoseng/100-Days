#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#
# # with open("high_score_save.txt", mode="w") as file:
# with open('Input/Names/invited_names.txt', 'r') as names:
#     raw_names_list = names.readlines()
#     names_list = []
#
#     for name in raw_names_list:
#         name = name.strip('\n')
#         names_list.append(name)
#     print(names_list)
#
#
# # for loop to replace [name] with a name from the readlines list.
# # make for loop create a different text document with their name.
# # https://www.kite.com/python/answers/how-to-replace-a-string-within-a-file-in-python
# for name in names_list:
#     reading_file = open('Input/Letters/starting_letter.txt', 'r')
#     new_file_content = ""
#     for line in reading_file:
#         new_line = line.replace("[name]", f"{name}")
#         new_file_content += new_line + "\n"
#     reading_file.close()
#     with open(f'Output/ReadyToSend/letter_for_{name}.txt', 'w') as ready_letter:
#         ready_letter.write(new_file_content)


PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

