x = int(input())
botoes=0


while(x!=0):
    if (x>=11):
        x-=11
        botoes+=1
    elif(x>=3 and x<11):
        x-=3
        botoes+=1
    elif(x<3):
        x-=1
        botoes+=1
print(botoes)