from collections import deque
pumps = int(input())

stations = deque([])

for _ in range(pumps):
    stations.append([int(el) for el in input().split()])


for big_circle in range(pumps):
    is_valid = True
    fuel = 0
    for small_circle in range(pumps):
        curr_station = stations[small_circle]
        curr_station_petrol, dist_to_next_st = curr_station[:]
        fuel += curr_station_petrol - dist_to_next_st
        if fuel < 0:
            stations.append(stations.popleft())
            is_valid = False
            break
    if is_valid:
        print(f'{big_circle}')
        break



'''
3
1 5
10 3
3 4
'''