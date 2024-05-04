inp = str(input())
inp = inp.split(",")

toDecrypt = inp[0]


#inp = "scammer2abc2"
#output = "scammerscammerabcscammerscammerabc"

#-----------------------------

copy = inp
res = ""


for i in range(len(toDecrypt)):
    if toDecrypt[i].isalpha():
        res += toDecrypt[i]
    elif toDecrypt[i].isnumeric():
        res = res*int(toDecrypt[i])
        
print(res[int(inp[1])-1])