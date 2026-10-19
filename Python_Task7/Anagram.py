import math
import os
import random
import re
import sys
from collections import Counter



def anagram(s):
    if len(s) % 2 != 0:
        return -1

    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]

    c1 = Counter(s1)
    c2 = Counter(s2)

    changes = 0

    for ch in c1:
        if c1[ch] > c2[ch]:
            changes += c1[ch] - c2[ch]

    return changes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for _ in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()