import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append((i, j, array[i][j]))
    visited[i][j] = 1
    while q:
        x, y, color = q.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny, array[nx][ny]))

n = int(input())
array = [list(input().strip()) for _ in range(n)]
cnt1, cnt2 = 0, 0
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 적록색약 아님
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt1 += 1
            bfs(i, j)

# G => R로 변환
for i in range(n):
    for j in range(n):
        if array[i][j] == 'G':
            array[i][j] = 'R'
# 적록색약
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt2 += 1
            bfs(i, j)

print(cnt1, cnt2)