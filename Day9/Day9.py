# programming_dictionary = {
#     "Bug": "A moth in a computer"
# }

# # Retrieve the value
# print(programming_dictionary["Bug"])

# # Add Data
# programming_dictionary["Loop"] = "Over and over again."

# # Loop through a dictionary
# for key in programming_dictionary:
#     print(key) # prints the key
#     print(programming_dictionary[key]) #prints the value





# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# # TODO-1: Create an empty dictionary called student_grades.

# student_grades = {}

# # TODO-2: Write your code below to add the grades to student_grades.👇

# for student in student_scores:
#     score = student_scores[student]
#     if score > 90: 
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
# # student_grades.update(student_scores)

# # 🚨 Don't change the code below 👇
# print(student_grades)




# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇

# def add_new_country(key_entry, visit_entry, city_entry):
    
#     # {
#     #     "country": key_entry,
#     #     "visits" : visit_entry,
#     #     "cities" : city_entry
#     #     }
    
#     new_country = {}
#     new_country["country"] = key_entry
#     new_country["visits"] = visit_entry
#     new_country["cities"] = city_entry

#     travel_log.append(new_country)
    
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)




# logo = '''
#                          ___________
#                          \         /
#                           )_______(
#                           |"""""""|_.-._,.---------.,_.-._
#                           |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\\
#                        .-------------.
#                       /_______________\\
# '''


# from os import system,name
# def clear():
#     if name == 'nt':
#         _ = system('cls')

# #HINT: You can call clear() to clear the output in the console.

# print(logo)
# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#     #Keeps adding key:values into bids dictionary
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
    
#     # Checks for other players. Will keep going until input = 'no'
#     should_continue = input("Are there any other players? Type 'yes' or 'no' : ")
#     if should_continue == 'no':
#         find_highest_bidder(bids)
#         bidding_finished = True
#     # Clears the terminal for the next person
#     elif should_continue == 'yes':
#         clear()



# # Check for highest bid.
# # Check each dictionary in the bidders list.
# # Look at the key/name and value/bid.
# # Compare the values to other values/bids in the others.
# # Print out the highest bidder's name and their bid amount.
