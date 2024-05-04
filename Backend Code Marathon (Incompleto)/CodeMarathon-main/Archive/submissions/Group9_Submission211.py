def get(f, n):
    cp = False
    pal = ""
    for s in f[::-1]:
        if s == str(n):
            cp = True
        elif s >= str(0) and s <= str(9) and cp:
            return pal
        elif cp:
            pal += s
    return pal

f = input()
g = get(f,1)
n = 2
out = ""
while g != "":
    out += g[::-1] + " "
    g = get(f, n)
    n += 1
print(out)