def main():
    pos, m1, m2 = input().split(",")
    pos = int(pos)
    m1 = int(m1)
    m2 = int(m2)
    i = 1
    j = 1
    l = []

    while len(l) < pos:
        m11 = m1 * i
        m22 = m2 * j
        if m11 < m22:
            if m11 not in l:
                l.append(m11)
            i += 1
        else:
            if m22 not in l:
                l.append(m22)
            j += 1
        l.sort()

    return l[pos - 1]


print(main())
