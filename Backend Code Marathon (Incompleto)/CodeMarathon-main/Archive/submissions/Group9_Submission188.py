n = [int(i) for i in input().split(',')]

solved = 0
i = 0
a = []

while len(a) < n[0] + 1:
    skrr = 0
    if i % n[1] == 0:
        a += [i]
        skrr = 1
    if i % n[2] == 0:
        if not skrr:
            a += [i]
    i += 1
    #print(a)

solved = a[n[0]]
print(solved)