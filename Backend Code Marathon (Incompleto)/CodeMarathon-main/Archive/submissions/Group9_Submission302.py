from time import sleep

i = int(input())
n = 0
while i > 0:
    i -= 1
    if n%10 < 6:
        n += 1
    elif n//10%10 < 6:
        n += 10
        n-= n%10
    elif n//100%10 < 6:
        n += 100
        n -= 66
    print(n, i)
    #sleep(0.5)
print(n)