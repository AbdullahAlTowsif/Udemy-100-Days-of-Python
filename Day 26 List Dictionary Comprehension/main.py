# List Comprehension
# Syntax: new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Towsif"
letter_list = [letter for letter in name]
print(letter_list)

range_list = [num * 2 for num in range(1,5)]
print(range_list)

# Conditional List Comprehension
# Syntax: new_list = [new_item for item in list if test]

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_name = [name.upper() for name in names if len(name) > 5]
print(long_name)


# Dictionary Comprehension
# To create a new dictionary
# Syntax: new_dict = {new_key : new_value for item in list}

import random
students_score = {student : random.randint(1, 100) for student in names}
print(students_score)


# To create a dictionary base on a existing dictionary
# Syntax: new_dict = {new_key : new_value for (key, value) in dict.items()}


# Conditional Dictionary Comprehension
# Syntax: new_dict = {new_key : new_value for (key, value) in dict.items() if test}

passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
print(passed_students)


student_dict = {
    "student": ["Angela", "Yu", "Towsif"],
    "score": [56, 76, 98]
}

# Looping through dictionaries
for (key, value) in student_dict.items():
    print(value)


import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Looping through a data frame

# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row)

