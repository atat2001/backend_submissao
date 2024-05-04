num = input()
cnt = 0

for ia in range(0 ,len(num), 1):
    for ib in range(len(num) - 1, -1, -1):
        if(ia < ib and num[ia] == num[ib]):
            cnt += 1

print(cnt)