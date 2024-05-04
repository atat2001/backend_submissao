inp = str(input())
inp = inp.split(",")

n1 = inp[0]
n2 = inp[1]
k = int(inp[2])

"""
queres um NR tal que:
    o tamanho do NR tem que ser igual a k;
"""

res = ""

fixed_i, fixed_j = 0, 0
len_n1, len_n2 = len(n1), len(n2)


def canChoose(whichNumber, ind):
    if whichNumber == 1:
        return len_n1-1-ind + len_n2-fixed_j >= k - len(res) - 1
    else:
        return len_n2-1-ind + len_n1-fixed_i >= k - len(res) - 1


def getMaxDigit():
    max = 0
    whichNumber = 1
    index = 0
    for i in range(fixed_i, len_n1):
        if not canChoose(1, i):
            continue
        if int(n1[i]) > max:
            max = int(n1[i])
            index = i
    for j in range(fixed_j, len_n2):
        if not canChoose(2, j):
            continue
        if int(n2[j]) > max:
            max = int(n2[j])
            whichNumber = 2
            index = j
    return max, whichNumber, index       
        
        

while True:
    max, whichNumber, index = getMaxDigit()
    if whichNumber == 1:
        fixed_i = index + 1
    else:
        fixed_j = index + 1
    res += str(max)
    if len(res) == k:
        break
    #print("current res: ", res, "\nfixed i: ", fixed_i, "\nfixed j: ", fixed_j)
    
    
print(res)