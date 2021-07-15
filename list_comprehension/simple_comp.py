#list comprehension
temps = [221, 234, 340, 230, -9999] # -9999 to simulate an unknown/ invalid data set

new_temps = []
for temp in temps:
    new_temps.append(temp /10)

print(new_temps)
#basic way to do it

#more concise way to do it 
new_temps2 = [temp / 10 for temp in temps]
print(new_temps2)
#define the new array with the calculation inside and an inline loop

#with conditionals
new_temps3 = [temp / 10 for temp in temps if temp != -9999]
print(new_temps3)

#advanced conditionals
new_temp4 = [temp / 10 if temp != -9999 else 0 for temp in temps]
print(new_temp4)
#if you need an if else inside a list comprehension, the loop MUST BE AT THE END