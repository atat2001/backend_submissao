num_lines = int(input())
goal = int(input())
starting_fuel = int(input())

stations = []

for _ in range(num_lines - 2):
	station = input()
	station_location, station_fuel = station.split(",")
	station_location = int(station_location)
	station_fuel = int(station_fuel)
	stations.append((station_location, station_fuel))

stations = sorted(stations, key=lambda x: x[0])


#import itertools


do_break_1 = False
do_break_2 = False
out = -1

def combinations(iterable, r):
	# combinations('ABCD', 2) --> AB AC AD BC BD CD
	# combinations(range(4), 3) --> 012 013 023 123
	pool = tuple(iterable)
	# first you create a tuple of the original input which you can refer later with 
	# the corresponding indices
	n = len(pool)
	# get the length of the tuple
	if r > n:
		return
	# if the length of the desired permutation is higher than the length of the tuple 
	# it is not possible to create permutations so return without doing something

	indices = list(range(r))
	# create the first list of indices in normal order ( indices = [0,1,2,3,...,r])
	# up to the desired range r

	yield tuple(pool[i] for i in indices)
	# return the first permutation which is a tuple of the input with the original 
	# indices up to r tuple(tuple[0], tuple[1],....,tuple[r])

	while True:
		for i in reversed(range(r)):
			# i will go from r-1, r-2, r-3, ....,0

			if indices[i] != i + n - r:
				# if condition is true except for the case 
				# that at the position i in the tuple the last possible 
				# character appears then it is equal and proceed with the character 
				# before which means that this character is replaced by the next 
				# possible one

				# example: tuple='ABCDE' so n = 5, r=3 indices is [0,1,2] at start i=2
				# yield (A,B,C)
				# indices[i] is 2 and checks if 2 != 4 (2 +5-3) is true and break
				# increase indices[i]+1 and yield (A,B,D)
				# indices[i] is 3 and checks if 3 != 4 (2 +5-3) is true and break
				# increase indices[i]+1 and yield (A,B,E) 
				# indices[i] is 4 and checks if 4 != 4 (2 +5-3) is false so next loop 
				# iteration:  i = 1 indices[i] is 1 and checks if 4 != 3 (1 +5-3) 
				# is true and break .... and so on

				break
		else:
			# when the forloop completely finished then all possible character 
			# combinations are processed and the function ends
			return

		indices[i] += 1 # as written proceed with the next character which means the 
						# index at i is increased
		for j in range(i+1, r): 
			indices[j] = indices[j-1] + 1 # all the following indexes are increased as 
										  # well since we only want to at following 
										  # characters and not at previous one or the
										  # same which is index at indice[i]
		yield tuple(pool[i] for i in indices)


for i in range(len(stations)):
	for subset in combinations(stations, i + 1):
		subset = list(subset) + [(goal, 0)]
		current_fuel = starting_fuel
		current_location = 0

		for station in subset:
			if current_location + current_fuel < station[0]:
				break

			current_fuel -= (station[0] - current_location)
			current_location += station[0]
			current_fuel += station[1]

			if current_fuel < 0:
				break

			if current_location >= goal:
				# nice, break?
				do_break_1 = True
				do_break_2 = True
				out = i + 1
				break

		if do_break_1:
			break

	if do_break_2:
		break


print(out)