import sys
input = sys.stdin.readline

def dfs(row):
  global answer
  if row == n:
    answer += 1
    return

  for col in range(n):
    if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
      cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
      dfs(row + 1)
      cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

n = int(input())
visited = [[0] * n for _ in range(n)]
answer = 0
cols = [False] * n # 열 체크
diag1 = [False] * (2 * n - 1) # '/' 대각선 체크 -> 각 좌표의 합이 같다
diag2 = [False] * (2 * n - 1) # '\' 대각선 체크 -> 각 좌표의 차가 같다
dfs(0)
print(answer)