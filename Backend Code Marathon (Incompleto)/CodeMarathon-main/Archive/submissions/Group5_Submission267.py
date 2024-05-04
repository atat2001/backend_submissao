inp = int(input())

if inp == 0:
    print(0)
    exit()

neg = False
if inp < 0:
    inp = -inp
    neg = True    
    
digitos = "0123456789"
res = ""
while inp > 0:
    q, r = divmod(inp, 7)
    res += digitos[r]
    inp = q

final = "".join(reversed(res))
if neg:
    final = "-" + final
    
print(final)
    