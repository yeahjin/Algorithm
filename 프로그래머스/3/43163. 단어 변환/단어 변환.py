from collections import deque

def valid(a,b):
    tmp = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            tmp += 1
    if tmp == 1:
        return True
    else:
        return False


def bfs(begin, target, words):
    q = deque()
    for i in words:
        if valid(begin, i):
            q.append((i, 1))
    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for i in words:
            if valid(word,i):
                q.append((i, cnt + 1))
    


def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    answer = bfs(begin, target, words)
    
    return answer