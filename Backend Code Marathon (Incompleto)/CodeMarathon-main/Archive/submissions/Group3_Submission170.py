user_input = int(input())

total=1
c = 0

for i in range(1,user_input):
    n = str(i)
    for c in n:
        if c =="0" or c =="1":
            total+=1
print(total)




#print(output)