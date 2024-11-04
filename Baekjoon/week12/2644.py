import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
  answer = -1
  q = deque()
  q.append((a, 0))
  visited[a] = 1
  while q:
    now, cnt = q.popleft()
    if now == b:
      answer = cnt
      break
    for i in graph[now]:
      if not visited[i]:
        visited[i] = 1
        q.append((i, cnt + 1))
  return answer
  
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for i in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)
print(bfs(a, b))