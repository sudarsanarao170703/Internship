def pangrams(s):
    letters = set(s.lower())

    if len(set('abcdefghijklmnopqrstuvwxyz') - letters) == 0:
        return "pangram"
    else:
        return "not pangram"

s = input()
print(pangrams(s))
