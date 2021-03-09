#AverageHeight

# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇

# num_inputs = 0
# height_total = 0
# for i in student_heights:
#   height_total += i
#   num_inputs += 1 
#   # print(num_inputs)
#   # print(height_total)

# average_height = float(height_total / num_inputs)
# print(round(average_height))


#High Score

# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# max_score = student_scores[0]
# for score in student_scores:
#   if score > max_score:
#     max_score = score
  
# print(max_score)



# # Add even numbers
# total = 0
# for num in range(0,101,2):
#   total += num
  
# print(total)





# #FizzBuzz

# for num in range(1, 101):
#   if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
#   elif num % 3 == 0:
#     print("Fizz")
#   elif num % 5 == 0:
#     print("Buzz")
#   else:
#     print(num)






# Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = input("How many letters would you like in your password?\n")
nr_symbols = input("How many symbols would you like in your password?\n")
nr_numbers = input("How many numbers would you like in your password?\n")

password_list = []
letterCount = 0
for letter in letters:
  while letterCount < int(nr_letters):
    random_letter_int = random.randint(0,len(letters) - 1)
    password_list.append(letters[random_letter_int])
    letterCount += 1

numberCount = 0
for num in numbers:
  while numberCount < int(nr_numbers):
    random_number_int = random.randint(0,len(numbers) - 1)
    password_list.append(numbers[random_number_int])
    numberCount += 1

symbolCount = 0 
for symbol in symbols:
  while symbolCount < int(nr_symbols):
    random_symbol_int = random.randint(0,len(symbols) - 1)
    password_list.append(symbols[random_symbol_int])
    symbolCount += 1

random.shuffle(password_list)

print(*password_list,sep = '')


#print out Password