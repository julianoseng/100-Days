
with open("file1.txt") as file_one:
    numbers_one = file_one.readlines()

with open("file2.txt") as file_two:
    numbers_two = file_two.readlines()

numbers_one = [int(num.strip()) for num in numbers_one]
numbers_two = [int(num.strip()) for num in numbers_two]

result = [int(num) for num in numbers_one if num in numbers_two]

# for num in numbers_one:
#     for numbers in numbers_two:
#         if numbers == num:
#             result.append(numbers)


print(result)
