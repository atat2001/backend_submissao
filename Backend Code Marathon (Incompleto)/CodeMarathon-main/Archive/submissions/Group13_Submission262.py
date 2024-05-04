x = int(input())
a = str(x)
lst=[]

for i in range(0,10):
    lst.append(0)

for i in range(len(a)):
    chr = int(a[i])
    lst[chr]+=1

mais_comum=0
index=0
for i in range(0,10):
    if (lst[i]>mais_comum):
        mais_comum=lst[i]
        index=i
print(index)