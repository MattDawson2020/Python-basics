#writing text 
with open("vegetables.txt", "w") as myfile:
    myfile.write('Tomato\nOnion\nCarrot')
    myfile.write('no Space')
    myfile.write("\nspace")
#using W mode lets you write a file, which creates a new file OR OVERWRITES EXISTING
#can only write one line unless you use \n

#appending to existing file
# with open('fruits.txt', 'x') as myfile:
#     myfile.write('cannot write this because file exists'), x does not overwrite

with open('fruits.txt', 'a') as myfile:
    myfile.write('Okra\n')
    myfile.seek(0) #reset the cursor to 0 so you can read the file
    content = myfile.read()

  #a flag lets you append to the end, remember the file cursor and whether you need a line break or not