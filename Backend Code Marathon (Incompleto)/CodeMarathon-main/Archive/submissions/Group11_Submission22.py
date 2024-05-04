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


import itertools


do_break_1 = False
do_break_2 = False
out = -1


for i in range(len(stations)):
	for subset in itertools.combinations(stations, i + 1):
		subset = list(subset) + [(goal, 0)]
		current_fuel = starting_fuel
		current_location = 0

		for station in subset:
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