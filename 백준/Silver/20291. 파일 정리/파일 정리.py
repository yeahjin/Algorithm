import sys

n = int(input())

d = {}

for i in range(n):
    book = sys.stdin.readline().rstrip().split(".")
    book_type = book[1]
    if book_type in d:
        d[book_type] += 1
    else:
        d[book_type] = 1

d = dict(sorted(d.items(), key=lambda x: x[0]))

for name, book_type in d.items():
    print(name, book_type)