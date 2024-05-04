#e2frase4Isto1uma3
frase = str(input(''))

dic = {}
pal = ""
index = ""
for elem in frase:
    if elem.isdigit():
        index += elem
    elif index != "":
        dic[index] = pal
        index = ""
        pal = ""
        pal += elem
    else:
        pal += elem

if index != "":
    dic[index] = pal
    index = ""
    pal = ""

m = 0
for key in dic:
    
    if int(key) > m:
        m = int(key)
res = ""

for i in range(1,m+1):
    key = str(i)
    res+= dic[key] + " "
print(res[:len(res)-1])
