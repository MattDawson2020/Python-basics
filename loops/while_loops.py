a = 0

#runs as long as a condition is true

while a < 10:
    print(a)
    a += 1

username = ''

while username != "pypy":
    username = input("Enter username:")


#break and continue
while True:
    username = input("Enter Username:")
    if username == 'pypy':
        break
    else:
        continue