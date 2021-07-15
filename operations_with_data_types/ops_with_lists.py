monday_temperatures = [9.1, 8.8, 7.5]
monday_temperatures.append(7.8)
#adds a new item to the end
print(monday_temperatures)

monday_temperatures.remove(8.8)
#removes specific value
print(monday_temperatures)

index = monday_temperatures.index(7.5, 0)
print(index)

print(monday_temperatures)
monday_temperatures.pop(-1)
print(monday_temperatures)
# removes items by index position

monday_temperatures.clear()
print(monday_temperatures)

# accessing list items
monday_temperatures = [9.1, 8.8, 7.5]
print(monday_temperatures[0]) #shorthand accessor
print(monday_temperatures.__getitem__(0)) # alternate

#accessing list slices
print(monday_temperatures[0:2]) #starts at first element and extracts 2
print(monday_temperatures[1:]) #starts at second and extracts entire list
#negative works as expected
print(monday_temperatures[-1])
#reverse slicing doesnt get the last item because it extracts a range between them 
print(monday_temperatures[:-1])
print(monday_temperatures[-2:])

#accessing characters and slices in strings
mystring = 'Hello, World!'
print(mystring[0])
#works the same as inside a list and lets you extract the first word
print(mystring[0:5])


#accessing items in dictionaries
student_grades = { "Dave": 9.1, "Tom": 8.8, "Steve": 7.5}
# print(student_grades[0]) returns an error because dictionaries dont have indexes, and are accessible via keys
print(student_grades['Dave'])

# can convert between data types, but going from dictionary to smaller data structure loses values
list_grade = list(student_grades)
print(list_grade)
tuple_grade = tuple(list_grade)
print(tuple_grade)
