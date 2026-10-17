n = int(input())
arr = map(int, input().split())
s=sorted(set(arr))
print(s[-2])