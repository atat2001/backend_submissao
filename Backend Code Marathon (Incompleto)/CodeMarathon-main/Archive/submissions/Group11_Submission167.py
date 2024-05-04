
num_galhos = int(input())

ze_turn = True


def play(num_galhos, ze_turn):
	if num_galhos > 6:
		return num_galhos - 3
	elif num_galhos <= 6 and num_galhos > 3:
		return num_galhos - 1
	else:
		print("perdedor" if ze_turn else "vencedor")
		return 0


if num_galhos < 1:
	print("perdedor")


while num_galhos != 0:

	if ze_turn:
		num_galhos = play(num_galhos, ze_turn)
		ze_turn = False
	else:
		num_galhos = play(num_galhos, ze_turn)
		ze_turn = True

#print()