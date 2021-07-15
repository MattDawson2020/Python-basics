student_grades = [9.1, 8.8, 7.5]
#use dir(list) to check if there is an average calculating method
# can use dir(__builtins__) to check built in functions, no average function but there is a sum

my_sum = sum(student_grades)
# len function calculates length/size of object, is a function in python NOT a method
my_avg = my_sum / len(student_grades)
print(my_avg)

username = 'Python3'
print(username.lower)
# returns the method itself = <built-in method lower of str object at 0x0000019CF38E5970>
print(username.lower())
# returns the result of calling the method = python3


#dictionary types, similar to a ruby hash/ JS object
student_grades = { "Dave": 9.1, "Tom": 8.8, "Steve": 7.5}
mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum / length
print(mean)


#tuple types
monday_temperatures = (1, 4, 5)
print(monday_temperatures)
monday_temperatures.append(5)
print(monday_temperatures)