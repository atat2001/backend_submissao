inp = int(input())

if inp == 0:
    print(0)
    exit()
    
digitos = "0123456789"
res = ""
while inp > 0:
    q, r = divmod(inp, 7)
    res += digitos[r]
    inp = q

print(int("".join(reversed(res))))
    