import sys

a = int(sys.stdin.readline().rstrip())

lst = []
lsta = []
for i in range(a):
    b = sys.stdin.readline().rstrip()
    lst.append(b.split())
for j in range(a):
    for k in range(len(lst[j][0])):
        if ord(lst[j][1][k]) >= ord(lst[j][0][k]):
            lsta.append(ord(lst[j][1][k])-ord(lst[j][0][k]))
        else:
            lsta.append((ord(lst[j][1][k])+26)-ord(lst[j][0][k]))

    print("Distances: ", end="")
    for g in range(len(lst[j][0])):
        print(lsta[g], end=" ")
    print("\n", end="")
    for h in range(len(lst[j][0])):
        lsta.pop()


