s, a = input().split(',')

b = ""

i = 0

while i < len(a):
    b += a[i]
    if i != len(a)-1 and a[i] == a[i+1]:
        i+=1
    i += 1

print(b)

print(s == b)
