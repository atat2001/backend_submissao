from math import factorial

user_input = input()

total = 0
d = {}

for c in user_input:
    if c not in d.keys():
        d[c] = 1
    else:
        d[c] += 1

for v in d.values():
    if v>1:
        total += ((v*(v-1))//2)

print(total)