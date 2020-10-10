e = input()

def countVowels(str):
    vowelCount = 0
    for c in str:
        if c == 'a':
            vowelCount += 1
        elif c == 'e':
            vowelCount += 1
        elif c == 'i':
            vowelCount += 1
        elif c == 'o':
            vowelCount += 1
        elif c == 'u':
            vowelCount += 1
    return vowelCount

print(e, "has", countVowels(e), "vowels in it.")