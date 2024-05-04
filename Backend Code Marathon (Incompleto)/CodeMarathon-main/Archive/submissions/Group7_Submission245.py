user_input = input().split(',')

counter,mins = 1,[]
val = None
for pos in user_input:
    npos = pos.split('(')
    nval = npos[0]
    if val!=None:
        if (int(nval)>=int(val)+10 or int(nval)<=int(val)-10) and npos[1]=='N)': mins.append(counter)
    if npos[1]=='P)': val = npos[0]
    counter+=1

print(mins)
    
