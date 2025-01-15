import sys
from collections import deque

input = sys.stdin.readline


def bfs(n, m, array, i, j):
  visited = [[0] * m for _ in range(n)]
  move = ((-1, 0), (1, 0), (0, -1), (0, 1))
  answer = 0

  # BFS로 만날 수 있는 사람 찾기
  q = deque([(i, j)])
  visited[i][j] = 1

  while q:
    x, y = q.popleft()
    if array[x][y] == 'P':
      answer += 1

    for dx, dy in move:
      nx, ny = x + dx, y + dy
      if 0 <= nx < n and 0 <= ny < m and array[nx][
          ny] != 'X' and not visited[nx][ny]:
        visited[nx][ny] = 1
        q.append((nx, ny))

  # TT
  if not answer:
    return 'TT'
  # answer
  return answer


def solution():
  n, m = map(int, input().split())
  array = [list(input().strip()) for _ in range(n)]

  # 도연이
  x, y = 0, 0
  for i in range(n):
    for j in range(m):
      if array[i][j] == 'I':
        x, y = i, j

  print(bfs(n, m, array, x, y))


if __name__ == '__main__':
  solution()
