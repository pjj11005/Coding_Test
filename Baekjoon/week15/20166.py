import sys
input = sys.stdin.readline

def dfs(x, y, index):
  global answer
  if index == len(s): # 문자열을 완성한 경우
    return 1
  if dp[x][y][index] != -1: # 문자열을 완성한 경우
    return dp[x][y][index]
    
  dp[x][y][index] = 0 # 초기화
  for dx, dy in move:
    nx, ny = (x + dx) % n, (y + dy) % m
    if s[index] == array[nx][ny]: # 다음 문자가 일치하는 경우만 탐색
      dp[x][y][index] += dfs(nx, ny, index + 1)
  return dp[x][y][index]
  
n, m, k = map(int, input().split())
array = [list(input().strip()) for _ in range(n)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
for _ in range(k):
  answer = 0
  s = input().strip()
  dp = [[[-1] * len(s) for _ in range(m)] for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if array[i][j] == s[0]:
        answer += dfs(i, j, 1)
  print(answer)