def weather_condition(temperature):
    if temperature > 7:
        return 'Warm'
    else:
        return 'Cold'

print(weather_condition(7))
#this code is not necessarily useful because it cant take any form of user input
# input() lets you take input from CLI/ terminal
temp = input('Enter temperature:')
#takes input and returns it AS A STRING
num_temp = int(temp) #also works with float()
print(weather_condition(num_temp))


#string formatting
