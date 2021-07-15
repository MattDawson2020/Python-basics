# python type is implicit
x = 10
y = '10'
sum1 = x + x
sum2 = y + y
print(sum1, sum2)

z = 10
print(z / 3)
print(type(x))

#list types
student_grades = [9.1, 8.8, 7.5]
print(student_grades)

#list keyword lets you generate a list with given parameters
#range keyword combination lets you generate specified list, optional third argument provides step
range_list = list(range(1, 15))
print(range_list)
step_list = list(range(0, 20, 5))
print(step_list)
word_list = list('Howdy' * 3)
print(word_list)

#attributes
print(dir(int))
help(str.upper)