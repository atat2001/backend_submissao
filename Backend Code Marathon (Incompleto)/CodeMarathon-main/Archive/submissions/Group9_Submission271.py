i = input().split(",")
n = []
for j in range(len(i)):
    n += [int(i[j])]

dic = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for i in n:
    dic[i] += 1

toPrint = ()
for d in dic:
    if dic[d] == 1:
        toPrint += (d,)

if len(toPrint) == 1:
    print(toPrint[0])
    exit()

print("(", end = "")
for n in toPrint[:-1]:
    print(n,end=",")

print(str(toPrint[-1])+")")