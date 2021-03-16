# #Functions


# #Create One
# def my_function():
#     print("Hello")
#     print("Bye")
    
# # Call the function
# my_function()




#Reeborg's World Hurdle 4 code:
#With each challenge, I am catching myself more and more.
#I keep telling myself "This is too complicated. Start over and make it work with simplicity."

# while not at_goal():
#     if wall_in_front() == True:
#         turn_left()
#     while wall_in_front() == False and not at_goal():
#         move()
#         if right_is_clear() == True:
#             turn_right()
#             move()
#             turn_right()
#             move()


#Reeborg's World Maze code:
#Holy shit this was hard but fun
# while not at_goal():
#     if front_is_clear() and right_is_clear():
#         move()
#     elif right_is_clear() == True and front_is_clear() == False:
#         turn_right()
#     elif front_is_clear() == False:
#         turn_left()
#     elif wall_on_right():
#         move() 