n, c = input().split(',')

if c not in '!,?,%,&,@,>'.split(','):
    print(False)
else:
    for i in range(int(n),0,-1):
        print(c*i)