def twoStrings(s1, s2):
    if set(s1) & set(s2):
        return "YES"
    return "NO"

q = int(input())

for _ in range(q):
    s1 = input().strip()
    s2 = input().strip()
    print(twoStrings(s1, s2))