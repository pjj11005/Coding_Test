import sys
from collections import deque

input = sys.stdin.readline


# 물채우기 가능한지 BFS 탐색
def bfs(i, j, h, array, visited, n, m):
  q = deque([(i, j)])
  move = ((-1, 0), (1, 0), (0, -1), (0, 1))
  visited[i][j] = 1
  points = [(i, j)]  # 물을 채울 위치들
  wall_height = float('inf')  # 벽의 최소 높이
  is_possible = True

  while q:
    x, y = q.popleft()

    # 테두리 체크
    if x == 0 or x == n - 1 or y == 0 or y == m - 1:
      is_possible = False

    for dx, dy in move:
      nx, ny = x + dx, y + dy
      if 0 <= nx < n and 0 <= ny < m:
        if array[nx][ny] > h:  # 높음
          wall_height = min(wall_height, array[nx][ny])
        elif array[nx][ny] == h and not visited[nx][ny]:  # 같음
          visited[nx][ny] = 1
          points.append((nx, ny))
          q.append((nx, ny))
        elif array[nx][ny] < h:  # 낮음(안됨)
          is_possible = False

  # 물 채우기 가능
  if is_possible and wall_height != float('inf'):
    total = 0
    for x, y in points:
      total += wall_height - array[x][y]
      array[x][y] = wall_height
    return total
  return 0


def solution():
  n, m = map(int, input().split())
  array = [list(map(int, input().strip())) for _ in range(n)]
  answer = 0

  # 낮은 높이 부터 물을 채워나감
  for h in range(1, 9):
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
      for j in range(m):
        if array[i][j] == h and not visited[i][j]:
          answer += bfs(i, j, h, array, visited, n, m)

  print(answer)


if __name__ == '__main__':
  solution()
