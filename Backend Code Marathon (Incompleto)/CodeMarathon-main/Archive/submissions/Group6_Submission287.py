inp = input()
final =[]
ls=[]
st = ""

for char in inp:
    st += char
    if char == ",":
        ls.append((st[-3],int(st[0:-4])))
        st = ""

ls.append((st[-2], int(st[0:-3])))

for cnt in range(len(ls)):
    tup = ls[cnt]
    if tup[0] == 'N' and abs(ls[cnt+1][1] - tup[1])>=10:
        final.append(cnt+1)
print(final)
