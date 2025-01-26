import sys

input = sys.stdin.readline


# DFS k 거리 개수 찾기
def dfs(x, y, depth, r, c, k, array, visited, move):
  global answer

  # 불가능
  if depth > k:
    return

  # 찾음
  if x == 0 and y == c - 1 and depth == k - 1:
    answer += 1
    return

  # 탐색
  for dx, dy in move:
    nx, ny = x + dx, y + dy
    if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and array[nx][ny] != 'T':
      visited[nx][ny] = 1
      dfs(nx, ny, depth + 1, r, c, k, array, visited, move)
      visited[nx][ny] = 0


def solution():
  global answer
  r, c, k = map(int, input().split())
  array = [list(input().strip()) for _ in range(r)]
  visited = [[0] * c for _ in range(r)]
  move = ((-1, 0), (1, 0), (0, -1), (0, 1))
  answer = 0

  # dfs 탐색
  visited[r - 1][0] = 1
  dfs(r - 1, 0, 0, r, c, k, array, visited, move)
  
  print(answer)


if __name__ == '__main__':
  solution()
