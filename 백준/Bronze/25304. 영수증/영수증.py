total = int(input())
n = int(input())
money = 0
for i in range(n):
    a, b = map(int, input().split())
    money += a*b

if money == total:
    print("Yes")
else:
    print("No")