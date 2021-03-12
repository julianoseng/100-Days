# print('Hello world!')

# -------------------------------------------------------------------------------------------------------------------------------------------------

# print("Welcome to the rollercoaster!")
# height = int(input("How tall are you in centimeters?\n"))

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("You are not tall enough to ride the rollercoaster.")



# -------------------------------------------------------------------------------------------------------------------------------------------------


# number = int(input("Hello, I will tell you if a given number is even or odd. Type a number below.\n"))

# if number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")


# -------------------------------------------------------------------------------------------------------------------------------------------------


# print("Welcome to the BMI calculator!")
# weight = float(input("Let's start. Please enter your weight in kilograms.\n"))
# height = float(input("Thank you for that. Now I need your height in meters.\n"))

# BodyMassIndex = round(weight / (height**2))

# if BodyMassIndex < 18.5:
#     interpretation = "underweight"
# elif BodyMassIndex >= 18.5 and BodyMassIndex < 25:
#     interpretation = "normal weight"
# elif BodyMassIndex >= 25 and BodyMassIndex < 30:
#     interpretation = "overweight"
# elif BodyMassIndex >= 30 and BodyMassIndex < 35:
#     interpretation = "obese"
# else:
#     interpretation = "clinically obese"    

# print(f"Thank you! Your BMI is {BodyMassIndex}. You are considered {interpretation}.")


# -------------------------------------------------------------------------------------------------------------------------------------------------


# year = int(input("Hello. Lets figure out if the year you enter is a leap year or not. Please enter the year below\n"))

# if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#     print("The year is a leap year.")
# elif year % 4 == 0 and year % 100 != 0:
#     print("The year is a leap year.")
# else:
#     print("The year is not a leap year.")    


# -------------------------------------------------------------------------------------------------------------------------------------------------


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza would you like? S, M, or L?")
# add_pepperoni = input("Do you want pepperoni? Y or N?")
# extra_cheese = input("Do you want extra cheese? Y or N?")

# if size == "S":
#     price = 15
# elif size == "M":
#     price = 20
# elif size == "L":
#     price = 25

# if add_pepperoni == "Y" and size == "S":
#     topping_price = 2
# elif add_pepperoni == "Y" and size == "M":
#     topping_price = 3
# elif add_pepperoni == "Y" and size == "L":
#     topping_price = 3
# else:
#     topping_price = 0

# if extra_cheese == "Y":
#     extra_cheese_price = 1
# else:
#     extra_cheese_price = 0

# final_bill = price + topping_price + extra_cheese_price

# print(f"Your final bill is ${final_bill}.")


# -------------------------------------------------------------------------------------------------------------------------------------------------


# import re

# name_one = input("Enter name one\n")
# name_two = input("Enter in name two\n")

# name_one_two_lowerCase = name_one.lower() + name_two.lower()

# nameOneTwoTensValue = sum(map(name_one_two_lowerCase.count, ['t','r','u','e']))
# nameOneTwoOnesValue = sum(map(name_one_two_lowerCase.count, ['l','o','v','e']))

# totalValue = (nameOneTwoTensValue * 10) + nameOneTwoOnesValue

# print(f"Your love compatibility is {totalValue}%.")              


# -------------------------------------------------------------------------------------------------------------------------------------------------


# Treasure Island

# choice_two = None
# choice_three = None

# print("Welcome to Treasure Island. Your mission is to find the treasure.")
# choice_one = input("You awaken at a crossroad. To your left is some trees. To your right is a beach. Which way do you choose? Left or Right?")
# if choice_one == "Left":
#     print("You fall into a trap and some trees fall on top of you. You are dead. GG noob.")
# elif choice_one == "Right":
#     choice_two = input("You walk to the beach, and you see an island. Do you A. swim across to the beach or B. find another way?")

# if choice_two == "A":
#     print("You try to swim across but a shark gets you. Ouch.")
# elif choice_two == "B":
#     choice_three = input("You manage to find a boat down the shore and drive it over to the island. On the island is a house. Do you go through door 1, 2, or 3?")
    
# if choice_three == "1":
#     print("The door had a claymore behind it. Bye byeeeee")
# elif choice_three == "2":
#     print("You open the door and walk through. Then you fall to your death because someone dug a giant hole. Whoopsies!!")
# elif choice_three == "3":
#     print("Holy shit, you found the treasure!!! YOU WIN!!!")