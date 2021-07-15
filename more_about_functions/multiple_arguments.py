#multiple arguments
def area(a, b):
    return a * b


#keyword and non keyword arguments
print(area(4,5)) #non keyword argument
print(area(b=4, a=8)) #keyword argument, similar to ruby hash arguments, position does not matter and can be specific

#default parameters
def default_area(a=5, b=5):
    return a * b
#default argument same as other languages

print(default_area())
print(default_area(10, 50))
print(default_area(b= 35, a= 70))

#functions with an arbitrary number of non-keyword argyments
# len('hello', 'hi') returns an error as len is supposed to take one argument
# print(2,4,6,'hi, ['fish']) will work because it expects multiple parameters

def mean(*args):# args is a conventional word to use
    return sum(args) / len(args) #this works because *args returns a tuple with the arguments
print(mean(6, 6, 6, 6, 6,))


#arbitrary number of keyword arguments
def key_mean(**kwargs): #double asterisk is all that is required but adding kw to be kwargs is convention
    return kwargs

# print(key_mean(6,6,6,6,))  returns an error because it needs keyword arguments
print(key_mean(a=1, b=2, c=3))
# returns {'a': 1, 'b': 2, 'c': 3}, dictionary with your arguments as keywords
