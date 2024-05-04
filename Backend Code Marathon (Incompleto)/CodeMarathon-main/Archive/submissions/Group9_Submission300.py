n, c = input().split(',')

if len(c) == 1 and c not in '!,?,%,&,@,>'.split(','):
    print(False)
else:
    for i in range(int(n),0,-1):
        print(c*i)
