user_input = input()
user_input = str(user_input)
counter = 0
res = 0
for i in user_input:
    i = int(i)
    if i != 0:
        if int(user_input[counter+1]) == 0:
            if int(user_input[counter + 2]) != 0:
                res += min(i,user_input[counter+2])
        elif int(user_input[counter+1]) < i:
            res += i-int(user_input[counter+1])
print(res)