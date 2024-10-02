import sys
input = sys.stdin.readline

def bfs(r, c, array):
  answer = 0
  q = set([(0, 0, array[0][0])])
  move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  while q:
    x, y, visited = q.pop()
    answer = max(answer, len(visited))
    for dx, dy in move:
      nx, ny = x + dx, y + dy
      if 0 <= nx < r and 0 <= ny < c and array[nx][ny] not in visited:
        q.add((nx, ny, visited + array[nx][ny]))

  return answer

r, c = map(int, input().split())
array = [list(input().strip()) for _ in range(r)]
print(bfs(r, c, array))