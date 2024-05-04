inp = input("")
lst = inp.split(",")
res = "true"
j = 0
for i in range(len(lst[0])):
    if (lst[0][i] != lst[1][j]):
        res = "false"
        break
    if (i == (len(lst[0]) - 1)):
        break 
    j += 1
    if (j == len(lst[1])):
        if (i != (len(lst[0]) - 1)):
            res = "false"
        break
    if (lst[0][i + 1] == lst[1][j]):
        continue
    j += 1
print(res)
    
