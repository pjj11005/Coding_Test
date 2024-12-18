import sys
from collections import defaultdict

# 입력 받기
n, m, k = map(int, input().split())
board = [input().strip() for _ in range(n)]
like = [input().strip() for _ in range(k)]

# 방향 설정 (상, 하, 좌, 우, 대각선 4방향)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

# 결과 저장용 딕셔너리
result = defaultdict(int)

# 백트래킹 함수
def dfs(x, y, current_string):
    # 현재 좌표의 문자를 추가
    current_string += board[x][y]
    
    # 만들 수 있는 최대 길이는 5
    if len(current_string) > 5:
        return
    
    # 현재까지 만든 문자열을 결과에 추가
    result[current_string] += 1
    
    # 8방향으로 이동하며 탐색
    for dx, dy in directions:
        nx = (x + dx) % n
        ny = (y + dy) % m
        dfs(nx, ny, current_string)

# 각 좌표에서 시작하여 DFS 탐색
for i in range(n):
    for j in range(m):
        dfs(i, j, "")

# 좋아하는 문자열의 등장 횟수 출력
for word in like:
    print(result[word])

# 53% 시간 초과과
# import sys
# input = sys.stdin.readline

# def dfs(x, y, index):
#   global answer
#   if index == len(s): # 문자열을 완성한 경우
#     return 1
#   if dp[x][y][index] != -1: # 문자열을 완성한 경우
#     return dp[x][y][index]
    
#   dp[x][y][index] = 0 # 초기화
#   for dx, dy in move:
#     nx, ny = (x + dx) % n, (y + dy) % m
#     if s[index] == array[nx][ny]: # 다음 문자가 일치하는 경우만 탐색
#       dp[x][y][index] += dfs(nx, ny, index + 1)
#   return dp[x][y][index]
  
# n, m, k = map(int, input().split())
# array = [list(input().strip()) for _ in range(n)]
# move = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
# for _ in range(k):
#   answer = 0
#   s = input().strip()
#   dp = [[[-1] * len(s) for _ in range(m)] for _ in range(n)]
#   for i in range(n):
#     for j in range(m):
#       if array[i][j] == s[0]:
#         answer += dfs(i, j, 1)
#   print(answer)