n = [int(i) for i in input().split(',')]

solved = 0
i = 1
a = []

while not solved:
    if i % n[1] == 0 and i != n[1]:
        solved = i
        break
    if i % n[2] == 0 and i != n[2]:
        solved = i
        break
    i += 1

print(solved)