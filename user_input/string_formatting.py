user_input = input("Enter your name:")
message = "Hello %s!" % user_input
# %s keyword/ escape characters than lets you define a % operator later as a variable/ element to sub in
print(message)

message2 = "Hello %s" % 1234
print(message2)

message3 = f"Hello {user_input}"
#this is a new way of doing it introduced in python 3.6, to be more easily recognised by developers of other languages
print(message3)

#multiple variables
user_input2 = input("What is your surname:")
concat_message  = "Hello %s %s" %(user_input, user_input2) 
#you can use multiple placeholders with multiple variables
print(concat_message)

#updated concat message
updated_concat_message = f"Hello {user_input} {user_input2}"
#as long as the f is added you can use as many as you want
#this is better where versioning allowed because its easier to target exactly what you want with less code
print(updated_concat_message)