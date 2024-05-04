i = input()
n = []
for j in range(len(i)):
    n += [int(i[j])]

dic = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for i in n:
    dic[i] += 1

maxi = 0
maxx = 0
for d in dic:
    if dic[d] > maxx:
        maxx = dic[d]
        maxi = d
print(maxi)