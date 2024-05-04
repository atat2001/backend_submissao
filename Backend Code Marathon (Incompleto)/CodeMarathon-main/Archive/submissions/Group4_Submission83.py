num = int(input(''))


#13 12 11 10 9 8 7 6 5 4 3 2 1


count = 0
for number in range(num,0,-1):
    while number != 0:
        res = number%10
        if res == 1 or res == 0:
            count+=1
        number = number//10

print(count)