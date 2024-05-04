user_input = input().split(',')

nums = {}
for num in user_input:
    if num in nums: nums[num]+=1
    else: nums[num]=1

res,counter = [],1
while res==[]:
    for num in nums:
        if nums[num]==counter:
            res.append(num)
    counter+=1

if len(res)==1: print(''.join(res))
else: print('('+','.join(res)+')')

    
