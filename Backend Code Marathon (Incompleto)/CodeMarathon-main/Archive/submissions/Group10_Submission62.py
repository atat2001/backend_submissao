n = int(input())
goal = int(input())
current_gas = int(input())


stops = []
for _ in range(n-2):
  km, gas = input().split(",")
  km, gas = int(km), int(gas)

  stops.append((km, gas))

#find
stopped_for_gas = 0
if current_gas > goal:
  print(stopped_for_gas)
else:
  needed = goal - current_gas
  for stop in stops:
    if stop[0] <= current_gas and stop[1] >= needed:
      current_gas += stop[1]
      stopped_for_gas += 1


print(stopped_for_gas)