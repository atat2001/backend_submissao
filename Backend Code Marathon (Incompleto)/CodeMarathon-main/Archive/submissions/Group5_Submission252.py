inp = int(input())


digitos = "0123456789"
res = ""
while inp > 0:
    q, r = divmod(inp, 7)
    res += digitos[r]
    inp = q

print(int("".join(reversed(res))))
    