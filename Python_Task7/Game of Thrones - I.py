from collections import Counter

def gameOfThrones(s):
    freq = Counter(s)

    odd = sum(1 for count in freq.values() if count % 2 != 0)

    return "YES" if odd <= 1 else "NO"

s = input().strip()
print(gameOfThrones(s))