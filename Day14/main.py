import game_data
import random

#Pull random stuff from data list
def random_data():
    random_number = random.randint(0,len(game_data.data) - 1)
    random_data = game_data.data[random_number]
    
    name = random_data['name']
    follower_count = random_data['follower_count']
    description = game_data.data[random_number]['description']
    country = game_data.data[random_number]['country']
    
    return name,follower_count,description,country
    

# print(random_data()[0])


# print(game_data.logo)
print(f"Compare A: {random_data()[0]} {random_data()[1]}")





# Pulling a value from the data list in the dictionaries
# print(game_data.data[0]['name'])