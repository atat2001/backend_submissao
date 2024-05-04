n = [int(i) for i in input().split(',')]

solved = 0
i = 1
a = []

while not solved:
    if i % n[1] == 0 and i not in n:
        solved = i
        break
    if i % n[2] == 0 and i not in n:
        solved = i
        break
    i += 1

while len(a) < n[0] + 1:
    skrr = 0
    if i % n[1] == 0 and i != n[1]:
        a += [i]
        skrr = 1
    if i % n[2] == 0 and i != n[2]:
        if not skrr:
            a += [i]
    i += 1

print(solved)