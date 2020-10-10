e = input()

def hasVowels(str):

    for c in str:
        if c == 'a':
            return True
        elif c == 'e':
            return True
        elif c == 'i':
            return True
        elif c == 'o':
            return True
        elif c == 'u':
            return True
    return False

while hasVowels(e) != True:
    print("This is not a word")
    e = input()
    hasVowels(e)

print("This is a word!")