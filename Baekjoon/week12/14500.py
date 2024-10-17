# 220ms
import sys
input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx): #가지치기 코드
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)

''' 내 풀이 : 6684ms
import sys
input = sys.stdin.readline

def dfs(x, y, total, depth):
  global answer
  if depth == 3:
    answer = max(answer, total)
    return

  for dx, dy in move:
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
      if depth == 1: # 자동차 모양 생성
        visited[nx][ny] = 1
        dfs(x, y, total + array[nx][ny], depth + 1)
        visited[nx][ny] = 0
      visited[nx][ny] = 1
      dfs(nx, ny, total + array[nx][ny], depth + 1)
      visited[nx][ny] = 0
    
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0
for i in range(n):
  for j in range(m):
    visited[i][j] = 1
    dfs(i, j, array[i][j], 0)
    visited[i][j] = 0
print(answer)
'''