from collections import Counter

X = int(input())
shoe_sizes = list(map(int, input().split()))
N = int(input())

available = Counter(shoe_sizes)
total_money = 0

for _ in range(N):
    size, price = map(int, input().split())

    if available[size] > 0:
        total_money += price
        available[size] -= 1

print(total_money)