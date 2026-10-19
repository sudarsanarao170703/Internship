def gemstones(arr):
    common = set(arr[0])

    for rock in arr[1:]:
        common &= set(rock)

    return len(common)

n = int(input())
arr = [input().strip() for _ in range(n)]

print(gemstones(arr))