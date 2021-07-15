# my_file = open("C:/Users/mattd/Desktop/Projects/Python-mega course/basics/file_processing/fruits.txt")
# need to use this path if running file outside of direct directory
my_file = open("fruits.txt")
#this one works ONLY when you are inside file_processing directory

# print(my_file.read())
# print(my_file.read())
#does not print twice because file cursor is at the end of the file and cannot find the text

content = my_file.read()
print(content)
print(content)
#will print as many times as you want because it refers to saved variable

#open file is stuck in memory until you close it, you can just work with the variable from here
my_file.close()

#opening files using 'with context manager'
with open("fruits.txt") as myfile:
    output = myfile.read()

print(output, 'here')
#allows you to open and store a file variable concisely inside a function block, which closes it for you


