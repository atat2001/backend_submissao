
s = str(input('')).split(',')

nums = [int(s[i]) for i in range(len(s))]


dic = {}

for num in nums:
    if num in dic:
        dic[num] +=1
    else:
        dic[num] = 0

pattern = 0
for key in dic:
    value = dic[key]
    if value > pattern:
        pattern = value
res = []
for num in nums:
    if dic[num] != pattern and ((res and res[len(res)-1] != num) or not res):
        res.append(num)

if len(res) == 1:
    print(res[0])
else:
    out = "("
    for elem in res:
        out+=str(elem)+","
    out = out[:len(out)-1]
    out+=")"
    print(out)
