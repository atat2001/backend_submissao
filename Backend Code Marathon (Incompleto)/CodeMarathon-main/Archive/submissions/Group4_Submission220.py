values = str(input())

beg = []
h = []
end = []
points = ""

for c in range(0, len(values), 4):
	beg.append(int(values[c]))
	h.append(int(values[c+1]))
	end.append(int(values[c+2]))
	

h_p = [0,0,0,0,0,0,0,0,0]
i_p = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
for i in range(9):
	for j in range(len(beg)):
		if beg[j] <= i+1 and end[j] >= i+1:
			if h_p[i] < h[j]:
				i_p[i] = j
				h_p[i] = h[j]

h = 0
current = -1

for i in range(9):
	if current != i_p[i]:
		if current == -1 and beg[i_p[i]] == i+1:
			points+=str(i+1)+str(0)+","
			points+=str(i+1)+str(h_p[i])+","
			
		else:
			points+=str(i)+str(h_p[i-1])+","
			points+=str(i)+str(min(h_p[i], h_p[i-1]))+","
		current=i_p[i]

	if i==8 and current!=-1:
		points+= str(i+1)+str(h_p[i])+","
		points+= str(i+1)+str(0)+","

	elif current != i_p[i+1] and beg[i_p[i+1]]==i+2:
		points+= str(i+1)+str(h_p[i])+","
		points+= str(i+1)+str(0)+","


	if end[current] == i+1:
		current = -1

print(points[:-1])





