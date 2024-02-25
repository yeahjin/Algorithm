n = int(input())
l1 = list(map(int, input().split()))
l2 = []

idx = 1

while l1:
    if l1[0] == idx:
        idx += 1
        l1.pop(0)
    else:
        l2.append(l1.pop(0))

    while l2:
        if l2[-1] == idx:
            idx += 1
            l2.pop()
        else:
            break

if not l2:
    print("Nice")
else:
    print("Sad")