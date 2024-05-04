def get_num(s, i):	
	res=0
	while type(s[i]) in str(range(10)):
		res = res*10+int(s[0])
		s = s[i:]
		i+=1
	return i

values = str(input())
d = []
i = 0

while i < len(values):
	get_num(values, i)


