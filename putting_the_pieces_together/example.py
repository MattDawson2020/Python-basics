#define function to parse inputs into desired output
def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    interrogatives = ('who', 'what', 'where', 'why', 'when', 'how')
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

#create empty container
results = []

#append formatted input into container unless they type keyword
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

#join the results onto a spaced string to have them join with a space
print(" ".join(results))
#join is defined as a str function in  python so you join on the string and provide list as an argument