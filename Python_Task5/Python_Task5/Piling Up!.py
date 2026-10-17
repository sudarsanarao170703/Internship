from collections import deque
T = int(input())
for _ in range(T):
    n = int(input())
    cubes = deque(map(int, input().split()))
    top = float('inf')
    while cubes:
        if cubes[0] >= cubes[-1]:
            chosen = cubes.popleft()
        else:
            chosen = cubes.pop()
        if chosen > top:
            print("No")
            break
        top = chosen
    else:
        print("Yes")