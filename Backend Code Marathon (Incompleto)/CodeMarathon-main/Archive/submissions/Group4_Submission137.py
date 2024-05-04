def ccw(A,B,C):
    return (C[0]-A[0]) * (B[1]-A[1]) > (B[0]-A[0]) * (C[1]-A[1])

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)



path = str(input(''))

path = path.split(',')

dirs = [(1,0),(0,-1),(-1,0),(0,1)]
index = 0

walk = []
prevPoint = (0,0)
dir = (1,0)
for elem in path:
    num = int(elem)
    newPoint = (prevPoint[0]+dir[0]*num,prevPoint[1]+dir[1]*num)
    walk.append([prevPoint,newPoint])
    prevPoint = newPoint
    index+=1
    if index == 4:
        index = 0
    dir = dirs[index]

numOfWalks = len(walk)
numOfIntersecs = 0
for i in range(numOfWalks-1):
    for j in range(i+1,numOfWalks):
        if i == j:
            continue
        if walk[i][0] == walk[j][0] or walk[i][0] == walk[j][1] or walk[i][1] == walk[j][0] or walk[i][1] == walk[j][1]:
            continue
        if intersect(walk[i][0],walk[i][1],walk[j][0],walk[j][1]):
            numOfIntersecs+=1

print(numOfIntersecs)
