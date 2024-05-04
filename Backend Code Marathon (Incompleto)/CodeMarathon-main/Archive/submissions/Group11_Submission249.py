
stuff = input()


n, char = stuff.split(",")
n = int(n)


if char not in ("!","?","%","&","@",">"):
	print("false")
else:
	for i in range(n):
		print(char * (n - i))
