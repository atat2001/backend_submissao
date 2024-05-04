def calcStops(kmGoal, gas, stops) -> int:
    count = 0
    total = gas
    stopId = 0
    while total < kmGoal:
        for stop in stops:
            stopId += 1
            if gas > stop[1]:
                gas = gas - stop[0] + stop[1]
                total += stop[0]
                count += 1
                break
            elif stopId == len(stops):
                # print(-1)
                return -1

    # print(count)
    return count


def main():
    stopsN = int(input()) - 2
    final = int(input())
    initial = int(input())
    stops = []
    for _ in range(stopsN):
        kmToStop, gas = input().split(",")
        stops.append((int(kmToStop), int(gas)))
        stops.sort(key=lambda y: y[0])
        stops.reverse()

    return calcStops(final, initial, stops)


main()
