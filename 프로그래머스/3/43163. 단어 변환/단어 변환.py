from collections import deque
def compare(x,y):
    cnt = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def bfs(begin,words,target):
    q = deque()
    
    q.append((begin,0))
    
    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for i in words:
            if compare(i, word):
                q.append((i, cnt + 1))
    

def solution(begin, target, words):
    if target not in words:
        return 0
    answer = bfs(begin,words,target)
    return answer