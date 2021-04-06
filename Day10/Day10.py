# # Functions with Outputs

 

# def format_name(f_name, l_name):

#     if f_name == "" or l_name == "":

#         return "You didn't provide valid inputs."

#     f_name = f_name.title()

#     l_name = l_name.title()

#     return f"{f_name} {l_name}"

 

# formatted_string = format_name("julIAN", "oSENg")

# print(formatted_string)

# print(format_name("julIAN", "oSENg"))

 

# print(format_name(input("What is your first name? "),

#                   input("What is your last name? ")))




# # Days in a month

 

# def is_leap(year):

#     # year = int(input("Hello. Lets figure out if the year you enter is a leap year or not. Please enter the year below\n"))

#     if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:

#         return True # it is a leap year

#     elif year % 4 == 0 and year % 100 != 0:

#         return True # it is a leap year

#     else:

#         return False # it is NOT a leap year




# def days_in_month(year, month):

#     if month > 12 or month < 1:

#         return "Invalid Month"

#     if year < 0:

#         return "Invalid Year"

#     month_days = [31,28,31,30,31,30,31,31,30,31,30,31]    

#     if is_leap(year) and month == 2:

#         return 29

#     return month_days[month - 1]

    

# year = int(input("Enter a year: "))

# month = int(input("Enter a month: "))

# days = days_in_month(year, month)

# print(days)





# Calculator

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    #Prints out all keys from operations dictionary
    for key in operations:
        print(key)

    #Request user input to figure out which operation they want to perform
    operation_symbol = input("Pick an operation from the lines above: ")

    #Ask for user input
    num1 = float(input("What is the first number? : "))
    num2 = float(input("What is the second number? : "))

    # Set the calculation_function to the operations key value.
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1,num2)

    #Prints out the entire operation and answer.
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    keep_going = True
    while keep_going is True:
        want_to_continue = input(f"Type 'y' to continue calculating with {first_answer} or type 'n' to start fresh. : ")
        if want_to_continue == 'y':
            operation_symbol = input("Pick another operator from the lines above: ")
            num3 = float(input("What is the next number? : "))
            calculation_function = operations[operation_symbol]
            second_answer = calculation_function(first_answer, num3)
            print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
            first_answer = second_answer
        else:
           keep_going = False
           calculator()

calculator()
# Recursion!!!!! WOOOO