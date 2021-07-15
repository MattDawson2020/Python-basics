
#third party modules
#pip with version command lets you install librarys, i.e pip3 pandas  installs panda library
# needed to add --user flag to the end due to administrator issue
import os
import time
import pandas #still need to import a thirty party package when installed

# while True:
#     if os.path.exists('../files/temps_today.csv'):  #only works when you are in same directory
#         with open('../files/temps_today.csv') as file:
#             data = pandas.read_csv("../files/temps_today.csv")
#             print(data.mean())
#     else:
#         print("file does not exist")
#         time.sleep(10)

while True:
    if os.path.exists('C:/Users/mattd/Desktop/Projects/Python-mega course/basics/files/temps_today.csv'):
        with open('C:/Users/mattd/Desktop/Projects/Python-mega course/basics/files/temps_today.csv') as file:
            data = pandas.read_csv("C:/Users/mattd/Desktop/Projects/Python-mega course/basics/files/temps_today.csv")
            print(data.mean()['st1'])
    else:
        print("file does not exist")
        time.sleep(10)

#this version works when run anywhere, possible issue with python installation and PATH
