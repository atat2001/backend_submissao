inp = str(input())
inp = inp.split(",")


def multiples(m, count):
    mults = []
    for i in range(1, count+1):
        mults.append(i*m)
    return mults



nrs = [int(inp[0]), int(inp[1]), int(inp[2])]
maxNr = max(nrs)


multsNr1 = multiples(nrs[1], nrs[0])
multsNr2 = multiples(nrs[2], nrs[0])

multsNr = multsNr1 + multsNr2
multsNr.sort()

#print(multsNr)
print(multsNr[nrs[0]-1])
    
    