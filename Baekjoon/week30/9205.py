import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y, fx, fy, n, cvs):
  q = deque([(x, y)])
  visited = [0] * n  # 편의점 방문 배열

  while q:
    a, b = q.popleft()

    # 페스티발 도착
    if abs(a - fx) + abs(b - fy) <= 1000:
      return 'happy'

    # 도달 가능한 편의점으로 이동
    for i in range(n):
      if not visited[i]:
        nx, ny = cvs[i]
        if abs(a - nx) + abs(b - ny) <= 1000:
          visited[i] = 1
          q.append((nx, ny))

  return 'sad'


def solution():
  for _ in range(int(input())):
    n = int(input())
    x, y = map(int, input().split())
    cvs = []
    for _ in range(n):
      a, b = map(int, input().split())
      cvs.append((a, b))
    fx, fy = map(int, input().split())
    print(bfs(x, y, fx, fy, n, cvs))


if __name__ == '__main__':
  solution()
