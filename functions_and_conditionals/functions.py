## custom functions
def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean
#only one space required, but 4 (2 indents) is common/ best practice

list = [10, 20, 30, 40, 50]
print(mean(list))

list2 = [1.5, 2.5, 6.7, 3.6, 2.6, 3.6]
print(mean(list2))

def noneMean(mylist):
    the_mean = sum(mylist) / len(mylist)
    print(the_mean)

print(noneMean(list))
# returns none because there is no return statement, result of print is a none object

