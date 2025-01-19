import sys
from collections import deque

input = sys.stdin.readline


# BFS 탐색
def bfs(n, m, graph):
  visited = [0] * (n + 1)
  q = deque([1])
  visited[1] = 1
  answer = 0

  while q:
    x = q.popleft()
    if x != 1:
      answer += 1

    for i in graph[x]:
      if not visited[i]:
        visited[i] = 1
        q.append(i)

  return answer


def solution():
  n = int(input())
  m = int(input())
  graph = [[] for _ in range(n + 1)]
  for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

  print(bfs(n, m, graph))


if __name__ == '__main__':
  solution()
