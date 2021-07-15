#import
import sys #imports tuple that holds module names as an attribute
print(sys.builtin_module_names)

import time #import specific module
print(dir(time)) #show module methods

print('Now')
time.sleep(10)
print('After')


#standard python modules
import os
import time

while True:
    if os.path.exists('filename/here'):
        with open('filename/here') as file:
            print(file.read())
    else:
        print("file does not exist")
        time.sleep(10)

#this code can be used to use the PATH module method to check if a file exists,
# so that a program will not shut down if a file cant be found

