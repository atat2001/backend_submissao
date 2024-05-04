x = str(input())
a = int(x)
dig=0

while (a!=0):
    for i in x:
        if (i=='0' or i=='1'):
            dig+=1
    a-=1
    x=str(a)
print(dig)

