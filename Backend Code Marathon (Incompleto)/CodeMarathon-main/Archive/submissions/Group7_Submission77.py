user_input = int(input())

count = 0
while user_input>0:
    current = user_input
    while current>=10:
        if current%10==1 or current%10==0: count+=1
        current//=10
    if current==1 or current==0: count+=1
    user_input-=1
print(count)
