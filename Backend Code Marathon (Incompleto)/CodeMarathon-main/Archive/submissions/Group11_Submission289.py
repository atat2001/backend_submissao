
stuff = input()
stuff = int(stuff)


count = 0

while stuff != 0:
	if stuff >= 11:
		stuff -= 11
	elif stuff >= 3:
		stuff -= 3
	else:
		stuff -= 1

	count += 1

print(count)