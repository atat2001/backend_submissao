st = input().split(",")
for i in range(len(st)):
    st[i] = int(st[i])

#inicio ou fim entre segmento do outro
blackList = []
points = []

for i in range(len(st)):
    if st[i]//100 * 10 not in points:
        points += [st[i]//100 * 10]
    if st[i]//100 * 10 + st[i]//10%10 not in points:
        points += [st[i]//100 * 10 + st[i]//10%10]
    if st[i]%10 * 10 + st[i]//10%10 not in points:
        points += [st[i]%10 * 10 + st[i]//10%10]
    if st[i]%10*10 not in points:
        points += [st[i]%10*10]

    st2 = st[:i] + st[i+1:]
    for j in range(len(st2)):
        xB = st2[j]//100
        xFB = st2[j]%10
        yB = st2[j]//10%10

        xA = st[i]//100
        xFA = st[i]%10
        yA = st[i]//10%10
        if xB == xA and yB > yA:
            blackList += [xA*10 + yA]
        if xB == xFA and yB > yA:
            blackList += [xFA*10 + yA]
        if xFB == xA and yB > yA:
            blackList += [xA*10 + yA]
        if xFB == xFA and yB > yA:
            blackList += [xFA*10 + yA]
        if xB < xA and xFB > xA:
            blackList += [xA*10]
        if xB < xFA and xFB > xFA:
            blackList += [xFA*10]
        if yA == yB and xB < xA and xFB > xA:
            blackList += [xA*10 + yA]
        if yA == yB and xB < xFA and xFB > xFA:
            blackList += [xFA*10 + yA]
        if xB < xFA and xFA < xFB and yB < yA:
            if xFA*10 + yB not in points:
                points += [xFA*10 +yB]
        if xB < xA and xA < xFB and yB < yA:
            if xFA*10 + yB not in points:
                points += [xA*10 +yB]
        if xB < xFA and xFA < xFB and yA < yB:
            if xFA*10 + yA not in points:
                points += [xFA*10 +yA]
        if xB < xA and xA < xFB and yA < yB:
            if xFA*10 + yA not in points:
                points += [xA*10 +yA]
        if xB < xA and xFB > xA and yB > yA:
            blackList += [xA*10 + yA]
        if xB < xFA and xFB > xFA and yB > yA:
            blackList += [xFA*10 + yA]

for v in blackList:
    i = 0
    while i < len(points):
        if v == points[i]:
            del points[i]
            continue
        i += 1

points.sort()
for p in points[:-1]:
    print(p, end=",")

print(points[-1])