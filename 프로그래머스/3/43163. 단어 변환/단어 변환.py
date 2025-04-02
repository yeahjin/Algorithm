from collections import deque

def word_cnt(a,b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def bfs(a, words, target):
    q = deque()
    q.append((a,0))
    
    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for i in words:
            if word_cnt(i,word):
                q.append((i, cnt + 1))
    
    
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    answer = bfs(begin,words, target)
    return answer