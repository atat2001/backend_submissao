import string
from unicodedata import decimal

changes = 0

notIn = False

min = 8
max = 20
charMin = list(string.ascii_lowercase)
charMax = list(string.ascii_uppercase)
dec = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specChar = ['!','?','-'',"_","$","%",&']

pwd = input()

# 1st check

if (len(pwd) <= min and len(pwd) > max):
    changes += 1

# 2nd check

for l in pwd:
    if l in charMin:
        notIn = True
        break

if not notIn:
    changes += 1
else:
    notIn = False

for l in pwd:
    if l in charMax:
        notIn = True
        break

if not notIn:
    changes += 1
else:
    notIn = False

for l in pwd:
    if l in dec:
        notIn = True
        break

if not notIn:
    changes += 1
else:
    notIn = False

for l in pwd:
    if l in specChar:
        notIn = True
        break

if not notIn:
    changes += 1
else:
    notIn = False

# 3rd check

alreadyCheck = list()

for l in pwd:
    if pwd.count(l, 0, len(pwd)) > 5:
        if l in alreadyCheck:
            pass
        else:
            alreadyCheck.append(l)
            changes += 1

#4th check

alreadyCheck2 = list()
stg = ""

for l in pwd:
    stg = l * 3
    if stg in pwd:
        if l not in alreadyCheck2:
            alreadyCheck2.append(l)
            changes += 1

print(changes)
        


