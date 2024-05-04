values = str(input())
n1=""
n2=""
flag = False
for c in values:
	if c==",":
		flag = True
	elif flag == False:
		n1+=c
	else:
		n2+=c

j=0
flag = True

for i in range(len(n1)):
	if j == len(n2):
		flag = False
		break
	if n1[i]!=n2[j]:
		flag = False
		break

	while n2[j]==n1[i]:
		if j == len(n2)-1: 
			if i == len(n1)-2:
				flag = False
			break
		j+=1

if flag == True:
	print("true")
else:
	print("False")
