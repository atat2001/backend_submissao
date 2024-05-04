


inp = input("Insert numbers: ")


st = ""
final = []

for el in inp:
    st += el
    if el == ",":
        final.append(int(st))
        st = ""

vt = [0,0]
graph = []
counter = {}

def vectorsum(ls_1, ls_2):

    new_ls = []
    new_ls[0] = ls_1[0] + ls_2[0]
    new_ls[1] = ls_1[1] + ls_2[1]
    return new_ls

for cnt, num in enumerate(final):

    if num > 0:
        sign = True
    elif num == 0:
        continue
    else:
        sign = False

    if sign:

        tag = cnt % 4
        
        if tag == 0:
            new = vectorsum(vt, [0, num])
            for i in range(vt[1], vt[1]+num+1):
                graph.append([vt[0], i])
            vt = new
        
        elif tag == 1:
            new = vectorsum(vt, [-num, 0])

            for i in range(vt[0], vt[0]-num+1, -1):
                graph.append([i, vt[0]])
            vt = new


        elif tag == 2:

            new = vectorsum(vt, [0, -num])

            for i in range(vt[1], vt[1]-num+1, -1):
                graph.append([vt[0], i])
            vt = new


        elif tag == 3:

            new = vectorsum(vt, [num,0])

            for i in range(vt[0], vt[0]+num+1):
                graph.append([i, vt[0]])
            vt = new
    else:

        cnt = abs(cnt)

        tag = cnt % 4
        
        if tag == 0:

            new = vectorsum(vt, [0, -num])
            for i in range(vt[1], vt[1]-num+1, -1):
                graph.append([vt[0], i])
            vt = new
        
        elif tag == 1:
           
            new = vectorsum(vt, [num,0])
            for i in range(num, vt[0]+num+1):
                graph.append([i, vt[0]])
            vt = new

        elif tag == 2:

            new = vectorsum(vt, [0, num])
            for i in range(num, vt[1]+num+1):
                graph.append([vt[0], i])
            vt = new

        elif tag == 3:

            new = vectorsum(vt, [-num, 0])
            for i in range(vt[0], vt[0]-num+1, -1):
                graph.append([i, vt[0]])
            vt = new

for ls in graph:
    counter.update({ls : graph.count(ls) - 1})

final = sum(counter.values())

print(final)






