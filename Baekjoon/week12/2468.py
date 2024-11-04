import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j, height):
  q = deque()
  visited[i][j] = 1
  q.append((i, j))
  while q:
    x, y = q.popleft()
    for dx, dy in move:
      nx, ny = x + dx, y + dy
      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and array[nx][ny] > height:
        visited[nx][ny] = 1
        q.append((nx, ny))
  
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0
for height in range(101):
  count = 0
  visited = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if array[i][j] > height and not visited[i][j]:
        bfs(i, j, height)
        count += 1
  answer = max(answer, count)
print(answer)