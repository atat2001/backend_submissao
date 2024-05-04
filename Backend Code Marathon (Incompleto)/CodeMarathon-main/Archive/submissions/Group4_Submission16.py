def get_values(sulcos, num):
	if num==10:
		return 0
	s = 0
	prev = -1
	for i in range(len(sulcos)):
		if sulcos[i]>=num:
			if prev == -1:
				prev = i
			else:
				s += i-prev-1
				prev = i
	s += get_values(sulcos, num+1)
	return s

			






values = str(input())

sulcos = []
for value in values:
	sulcos.append(int(value))
		
print(get_values(sulcos, 1))
