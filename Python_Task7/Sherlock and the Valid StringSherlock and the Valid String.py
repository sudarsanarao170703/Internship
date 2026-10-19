from collections import Counter

def isValid(s):
    freq = Counter(s)
    values = list(freq.values())

    for ch in freq:
        freq[ch] -= 1

        temp = [v for v in freq.values() if v > 0]

        if len(set(temp)) == 1:
            return "YES"

        freq[ch] += 1

    if len(set(values)) == 1:
        return "YES"

    return "NO"