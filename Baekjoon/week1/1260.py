import sys
from collections import deque
input = sys.stdin.readline

def dfs(x):
    print(x, end=' ') # dfs 탐색 마다 출력
    visited[x] = 1
    
    for i in graph[x]:
        if not visited[i]:   
            dfs(i)
    
def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    
    while q:
        now = q.popleft()
        print(now, end=' ') # bfs 탐색마다 출력
        
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)



n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1): # 작은 수부터 탐색하도록 정렬
    graph[i].sort()

visited = [0] * (n + 1) # 방문 처리
dfs(start)
print()
visited = [0] * (n + 1) # 방문 처리
bfs(start)