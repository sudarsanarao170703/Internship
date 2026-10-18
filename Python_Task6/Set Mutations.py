n = int(input())
A = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    command, length = input().split()
    other_set = set(map(int, input().split()))

    if command == "update":
        A.update(other_set)

    elif command == "intersection_update":
        A.intersection_update(other_set)

    elif command == "difference_update":
        A.difference_update(other_set)

    elif command == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)

print(sum(A))