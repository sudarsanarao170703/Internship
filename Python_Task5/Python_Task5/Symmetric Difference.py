M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))
result = a.symmetric_difference(b)
for num in sorted(result):
    print(num)