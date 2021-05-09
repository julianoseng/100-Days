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
print(students_scores)
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

