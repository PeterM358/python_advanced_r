from collections import deque
jobs = deque(list(map(int, input().split(", "))))
#  jobs = [3, 1, 10, 1, 2]
job_index = int(input())
job_to_finish = jobs[job_index]
total_cycles = 0
sorted_jobs = deque(sorted(jobs))

while sorted_jobs:

    if sorted_jobs[0] <= job_to_finish:
        total_cycles += sorted_jobs.popleft()
    else:
        break

print(total_cycles)

'''
3, 1, 10, 1, 2
0
'''