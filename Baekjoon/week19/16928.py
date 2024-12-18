import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    answer = 0 # 답
    q = deque([(1, 0)]) # 현재 위치, 주사위 횟수
    visited[1] = 1
    while q:
        now, cnt = q.popleft()
        if now == 100: # 도달
            answer = cnt
            break

        for d in move: # 이동
            next = now + d
            if next <= 100 and not visited[next]:
                visited[next] = 1
                if array[next] > 0: # 뱀 or 사다리
                    next = array[next]
                    visited[next] = 1
                q.append((next, cnt + 1))
                
    return answer

n, m = map(int, input().split())
array = [0] * 101 # 사다리 or 뱀 정보
visited = [0] * 101 # 방문
move = (1, 2, 3, 4, 5, 6) # 이동

# 사다리
for _ in range(n):
    u, v = map(int, input().split())
    array[u] = v

# 뱀
for _ in range(m):
    u, v = map(int, input().split())
    array[u] = v

print(bfs())