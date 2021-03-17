# #Paint Calculation
# #Write your code below this line 👇

# import math
# # print(math.ceil(4.2))


# def paint_calc(height, width, cover):
    
#     number_of_cans = (test_h * test_w) / coverage
#     number_of_cans = math.ceil(number_of_cans)
#     print(f"You'll need {number_of_cans} cans of paint.")
    

# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)






# #Prime Number Checker 
# #Write your code below this line 👇

# def prime_checker(number):
#     divisible_by = 0
#     for num in range (1,101):
#         if number % num == 0:
#             divisible_by += 1
    
#     if divisible_by > 2:
#         print(f"{number} is not a prime number")
#     else:
#         print(f"{number} is a prime number")
            
# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)






# Caesar Cipher
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encrypt':
    encrypt(text, shift)

def encrypt(text, shift):
    
            
         