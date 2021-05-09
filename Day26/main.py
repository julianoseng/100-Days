# List Comprehension
# new_list = [new_item for item in list]

# Conditional List Comprehension
# new_list = [new_item for item in list if test]

# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}

# Conditional Dictionary Comprehension
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_scores = {student: random.randint(1, 100) for student in names}
# print(students_scores)
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)

# Iterate over a Pandas DataFrame
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key,  value) in student_dict.items():
#     print(value)  # or key


# Loop through dataframe
import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)  # or key
# pandas has built in method - Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row.score)  # or index or row
    if row.student == "Angela":
        print(row.score)

# for (index, row) in student_data_frame.iterrows():
# {new_key:new_value for (index, row) in data_frame.iterrows()}
