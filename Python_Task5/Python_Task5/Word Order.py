from collections import Counter
n = int(input())
words = [input() for _ in range(n)]
counts = Counter(words)
print(len(counts))
print(*counts.values())