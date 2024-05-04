inp = input()

num = ["0","1","2","3","4","5","6","7","8","9"]
ls = []
st = ""
final = ""

for char in inp:
    st += char
    if char in num:
        ls.append((st[-1], st[:-1]))
        st = ""
ls.sort()

for tup in ls:
    final += tup[1] + " "
final = final[:-1]

print(final)