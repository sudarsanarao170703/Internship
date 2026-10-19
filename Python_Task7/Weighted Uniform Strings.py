def weightedUniformStrings(s, queries):
    weights = set()

    current_weight = 0
    prev = ''

    for ch in s:
        value = ord(ch) - ord('a') + 1

        if ch == prev:
            current_weight += value
        else:
            current_weight = value

        weights.add(current_weight)
        prev = ch

    result = []

    for q in queries:
        result.append("Yes" if q in weights else "No")

    return result


if __name__ == '__main__':
    s = input().strip()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries.append(int(input().strip()))

    result = weightedUniformStrings(s, queries)

    print('\n'.join(result))