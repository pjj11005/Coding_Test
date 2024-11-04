import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    count = 0
    q = deque()
    q.append((i, j, 0))
    visited[i][j] = 1
    while q:
        x, y, cnt = q.popleft()
        count = max(count, cnt)
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny, cnt + 1))
    return count

n, m = map(int, input().split())
array = [list(input().strip()) for _ in range(n)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0
for i in range(n):
    for j in range(m):
        if array[i][j] == 'L':
            visited = [[0] * m for _ in range(n)]
            answer = max(answer, bfs(i, j))
print(answer)