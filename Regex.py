import re

file = open('email.html')
line = file.readline()
while line:
    line = file.readline()
    m = re.findall(r'(([\w.])+@([\w.])+)', line)

    for match in m:
        email, *_ = match
        print(email)
file.close()

