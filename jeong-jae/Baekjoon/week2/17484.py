import sys
from collections import deque

input = sys.stdin.readline

def solution(n, m, array):
  answer = int(1e9)
  direction = [(1, -1), (1, 0), (1, 1)]  # 왼쪽, 가운데, 오른쪽
  for i in range(m):
    q = deque()
    q.append((0, i, -1, array[0][i]))
    while q:
      x, y, direct, cost = q.popleft()
      if x == n - 1:
        answer = min(answer, cost)
      for j in range(3):
        if j != direct:
          nx, ny = x + direction[j][0], y + direction[j][1]
          if 0 <= nx < n and 0 <= ny < m:
            q.append((nx, ny, j, cost + array[nx][ny]))
  return answer

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, array))