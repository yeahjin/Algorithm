from collections import deque
import heapq
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
    # q = deque()
    q = []
    d = [1e9] * len(words)
    # v = [0] * len(words)
    for i in range(len(words)):
        if compare(begin,words[i]):
            # q.append((words[i],1))
            heapq.heappush(q,(1,words[i]))
            d[i] = 1
            # v[i] = 1
    while q:
        cnt, word = heapq.heappop(q)
        print(word)
        if word == target:
            return cnt
        for i in range(len(words)):
            if d[i] <= cnt:
                continue
            if compare(words[i],word):
                heapq.heappush(q,(cnt+1, words[i]))
                d[i] = cnt + 1
    return 0
                
    

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    answer = bfs(begin,words,target)

    
    return answer