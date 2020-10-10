List = []

e = input()

while e != "stop":
    List.append(e)
    e = input()
    e =  e.lower()

for i in range(len(List)):
    print(List[i])