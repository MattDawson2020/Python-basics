#for loop runs through a container/ object and ends when the end of object is reached
monday_temperatures = [9.1, 8.8, 7.6]

for temperature in monday_temperatures:
    print(round(temperature))
# simple and concise syntax, uses for and in keywords

for letter in 'Hello, World!':
    print(letter)

#iterating over dictionaries 

student_grades = { "Dave": 9.1, "Tom": 8.8, "Steve": 7.5}

for grade in student_grades.values():
    print(grade)

for student in student_grades.keys():
    print(student)
    
#you can iterate over dictionaries as long as you specify whether you are iterating over the keys or the values

for pair in student_grades.items():
    print(pair[0], pair[1])

# you can iterate over the dictionary and pick the key or value be specifying items()

for key, value in student_grades.items():
  print("{} achieved a {}".format(key, value))
#parallel looping lets you be smarter about it