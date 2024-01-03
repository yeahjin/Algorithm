def hanoi(n, s, e, c):
    if n == 1:
        print(s, e)
    else:
        hanoi(n - 1, s, c, e)
        print(s, e)
        hanoi(n - 1, c, e, s)


n = int(input())
print(2 ** n - 1)
if n <= 20:
    hanoi(n, 1, 3, 2)