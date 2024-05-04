string = input()
steps = []
path = [[0,0]]
index = [0,0]
for l in string:
    steps += [int(l)]

def move(s, pos, signal):
    global path
    global index
    res = 0
    for j in range(s):
        index[pos] += 1 * signal
        if index in path:
            res += 1
        elif index not in path:
            path += [index.copy()]
    return res

count = 0
state = "up"
for i in steps:
    if i == 0:
        continue
        
    if state == "up":
        count += move(i, 1, 1)
        state = "left"
    
    elif state == "left":
        count += move(i, 0, -1)
        state ="down"
    
    elif state == "down":
        count += move(i, 1, -1)
        state = "right"
    
    elif state == "right":
        count += move(i, 0, 1)
        state = "up"

print(count)
