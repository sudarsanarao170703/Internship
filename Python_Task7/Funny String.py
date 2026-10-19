def funnyString(s):
    r = s[::-1]

    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            return "Not Funny"

    return "Funny"

q = int(input())

for _ in range(q):
    s = input().strip()
    print(funnyString(s))