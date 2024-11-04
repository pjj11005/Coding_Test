import sys
from collections import deque
input = sys.stdin.readline

# 다 익었는지 확인
def check(array):
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if array[i][j][k] == 0: # 안 익음
          return False
  return True

def bfs(q):
  answer = 0
  while q:
    z, x, y, time = q.popleft()
    if answer < time:
      answer = time
    for dz, dx, dy in move:
      nx, ny, nz = x + dx, y + dy, z + dz
      if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and array[nz][nx][ny] == 0:
        array[nz][nx][ny] = 1
        q.append((nz, nx, ny, time + 1))

  if check(array): # 다 익음
    return answer
  else: # 다 안 익음
    return -1
    
m, n, h = map(int, input().split())
array = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# 이동 좌표
move = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
# 익은 토마토 위치 q에 저장
q = deque()
for i in range(h):
  for j in range(n):
    for k in range(m):
      if array[i][j][k] == 1:
        q.append((i, j, k, 0))

print(bfs(q))