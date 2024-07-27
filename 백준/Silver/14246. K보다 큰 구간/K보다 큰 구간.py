import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline().rstrip())

count = 0
total = 0
start = 0

for end in range(n):
    total += data[end]
    while total > k:
        total -= data[start]
        count += n - end
        start += 1
print(count)