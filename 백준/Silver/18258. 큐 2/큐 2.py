import sys
from collections import deque

input = sys.stdin.readline()

def push(x):
    l.append(x)

def size():
    global l
    return len(l)

def pop():
    global l
    ans = 0
    if len(l) == 0:
        return -1
    else:
        return l.popleft()

def empty():
    global l
    if len(l) == 0:
        return 1
    else:
        return 0

def front():
    global l
    if len(l)== 0:
        return -1
    else:
        return l[0]

def back():
    if len(l) == 0:
        return -1
    else:
        return l[-1]


n = int(input)
l = deque()
for i in range(n):
    input = sys.stdin.readline()
    tmp = input
    inputSplit = tmp.split()
    inp = inputSplit[0]

    if inp == 'push':
        push(inputSplit[1])
    elif inp == "pop":
        print(pop())
    elif inp == "size":
        print(size())
    elif inp == "empty":
        print(empty())
    elif inp == "front":
        print(front())
    elif inp == "back":
        print(back())