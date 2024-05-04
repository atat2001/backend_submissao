i = input()
n = []
for j in range(len(i)):
    n += [int(i[j])]

start = n[0]
del n[0]

while start < len(n):
    if n[start-1] == 0:
        print("false")
        exit()
    start += n[start-1]
print("true")