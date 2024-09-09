from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    visited = []
    n = len(begin)
    q = deque([(begin, 0)])
    while q:
        now, count = q.popleft()
        if now == target:
            answer = count
            break
        for word in words:
            temp = 0
            for i in range(n):
                if word[i] != now[i]:
                    temp += 1
            if temp == 1 and (word not in visited):
                visited.append(word)
                q.append((word, count + 1))
                
    return answer
