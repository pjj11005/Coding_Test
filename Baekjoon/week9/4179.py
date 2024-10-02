import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, fire):
  answer = 0
  
  q = deque()
  for a, b in fire:
    q.append((a, b, 'F', 0))
  q.append((x, y, 'J', 0))
  
  while q:
    x, y, type, time = q.popleft()
    if type == 'F': # F
      for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and array[nx][ny] != '#':
          visited[nx][ny] = 1
          array[nx][ny] = 'F'
          q.append((nx, ny, 'F', time + 1))
    else: # J
      if x == 0 or x == r - 1 or y == 0 or y == c - 1:
        return time + 1
      for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
          if not visited[nx][ny] and array[nx][ny] == '.':
            visited[nx][ny] = 1
            array[nx][ny] = 'J'
            q.append((nx, ny, 'J', time + 1))

  return 'IMPOSSIBLE'
        
r, c = map(int, input().split())
array = [list(input().strip()) for _ in range(r)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[0] * c for _ in range(r)]
x, y = 0, 0  # 지훈
fire = []  # 불의 좌표
for i in range(r):
  for j in range(c):
    if array[i][j] == 'J':
      x, y = i, j
      visited[i][j] = 1
    elif array[i][j] == 'F':
      fire.append((i, j))
      visited[i][j] = 1
print(bfs(x, y, fire))
