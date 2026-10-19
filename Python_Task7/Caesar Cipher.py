def caesarCipher(s, k):
    result = ""

    for ch in s:
        if ch.islower():
            result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        elif ch.isupper():
            result += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        else:
            result += ch

    return result


if __name__ == '__main__':
    n = int(input())
    s = input().strip()
    k = int(input())

    print(caesarCipher(s, k))