import math
import os
import random
import re
import sys
from collections import Counter
def makingAnagrams(s1, s2):
    count1 = Counter(s1)
    count2 = Counter(s2)

    deletions = 0

    for ch in set(count1.keys()).union(count2.keys()):
        deletions += abs(count1[ch] - count2[ch])

    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()