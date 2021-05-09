sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# print(sentence.split())
sentence_list = {word: len(word) for word in sentence.split()}
print(sentence_list)