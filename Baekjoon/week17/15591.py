import sys
from collections import deque
input = sys.stdin.readline

def solution(k, v):
    answer = 0 # 답
    visited = [False] * (n + 1) # 방문
    q = deque([v])
    visited[v] = True

    # BFS
    while q:
        now = q.popleft()
        for next_node, cost in graph[now]:
            if not visited[next_node] and cost >= k: # k이상 만 탐색
                visited[next_node] = True
                q.append(next_node)
                answer += 1

    return answer

n, Q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())
    print(solution(k, v))