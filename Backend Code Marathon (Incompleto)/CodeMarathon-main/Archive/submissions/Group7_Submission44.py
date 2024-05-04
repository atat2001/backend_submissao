user_input = input()
tinput=[]
for i in range(int(user_input)):
    a = input()
    tinput.append(a)

needed = int(tinput[0])-int(tinput[1])
end = int(tinput[0])
stops = tinput[2:]
count,diff=0,None

def next_stop(stops, needed, count, diff,end):
    if needed==None: return -1
    for stop in stops:
        s = stop.split(',')
        d = needed-int(s[1])
        if int(s[0])<(end-needed) and d<=0:
            count+=1
            return count
        if int(s[0])<=(end-needed) and d>0:
            count+=1
            diff=d
    return next_stop(stops, diff, count, None, end)


print(next_stop(stops, needed, count, diff, end))