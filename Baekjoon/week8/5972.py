import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def solution(n, m, graph):
  distance = [INF] * (n + 1)
  q = []
  heapq.heappush(q, (0, 1))
  distance[1] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue

    for i, cost in graph[now]:
      if distance[i] > cost + dist:
        distance[i] = cost + dist
        heapq.heappush(q, (cost + dist, i))
  return distance[n]
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
print(solution(n, m, graph))