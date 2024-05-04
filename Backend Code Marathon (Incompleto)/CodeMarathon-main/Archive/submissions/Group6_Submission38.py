

inp = str(input("Insert layout"))

ls = []

for count, el in enumerate(inp):
    ls[count] = el

bound, hgt ,val = 0
for i in range(len(ls)):
    if(ls[i]):
        upper = ls[i]
        for cnt,el in enumerate(ls[i:]):
            if el >= upper:
                lgt = cnt - i
                for j in ls[i:cnt+1]: 
                    hgt += upper - ls[j]
                val += min(0, lgt * hgt) 
                hgt = 0







    


