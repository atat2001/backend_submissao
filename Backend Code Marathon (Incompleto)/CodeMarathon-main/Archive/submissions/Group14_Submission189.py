def main():
    pos, m1, m2 = input().split(",")
    pos = int(pos)
    m1 = int(m1)
    m2 = int(m2)
    i = 0
    l = []
    while len(l) < pos:
        i += 1
        m11 = m1 * i
        m22 = m2 * i
        if m11 not in l:
            l.append(m11)
        if m22 not in l:
            l.append(m22)
        l.sort()
    return l[pos - 1]


print(main())
