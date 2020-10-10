List = []

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

while e != "stop":
    List.append(e)
    e = input()
    e =  e.lower()

total = 0

for i in range(len(List)):
    total += countVowels(List[i])

print(total)