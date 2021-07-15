#intro to conditionals 
def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

list = [10, 20, 30, 40, 50] #mean will work on this because it can calculate length of a list
student_grades = { "Dave": 9.1, "Tom": 8.8, "Steve": 7.5} # will not work here because the sum cannot add strings and numbers together

def smartmean(value):
    if type(value) == dict: # if block also needs its own indents to form the block, end conditional statements with colons
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean 
# returns to the original block because it is on the original indent and does not specify itself as a further conditional

print(smartmean(list))
print(smartmean(student_grades))

x,y = 2,3 # parallel assignment works
if x > y:
    print('x is greater than y')
elif x < y:
    print('y is greater than x')
else:
    print('x is equal to y')
#python equivalent of elseif/ else if is elif

message = "hello there"
 
if "hello" in message:
    print("hi")
else:
    print("I don't understand")
# in a shorthand for ruby include

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")

#and works like &&

x = 1
y = 2
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")

#or works like ||
