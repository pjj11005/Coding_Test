import sys
input = sys.stdin.readline

# 사각지대 계산
def check(array):
  count = 0
  for i in range(n):
    for j in range(m):
      if array[i][j] == 0:
        count += 1
  return count

# 감시 채우기
def fill(x, y, array, directs):
  for direct in directs:
    dx, dy = move[direct][0], move[direct][1]
    nx, ny = x, y
    while True:
      nx += dx
      ny += dy
      # 범위 밖
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        break
      # 벽 만남
      if array[nx][ny] == 6:
        break
      # 빈칸 감시로 채우기
      elif array[nx][ny] == 0:
        array[nx][ny] = 7

# dfs
def dfs(depth, array):
  global answer
  if depth == len(cctv):
    answer = min(answer, check(array))
    return
  # 복사
  array_copy = [row[:] for row in array]
  # cctv별 방향으로 감시 진행
  cctv_num, x, y = cctv[depth]
  for directs in mode[cctv_num]:
    fill(x, y, array_copy, directs)  # 현재 감시 방향들로 채우기
    dfs(depth + 1, array_copy)  # 다음 cctv 진행
    array_copy = [row[:] for row in array]  # 다시 현 시점으로

n, m = map(int, input().split())
array = []
cctv = []  # cctv
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 위, 우, 아래, 왼
# cctv index
mode = [
    [],
    [[0], [1], [2], [3]],  # 1
    [[1, 3], [0, 2]],  # 2
    [[0, 1], [1, 2], [2, 3], [3, 0]],  # 3
    [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]],  # 4
    [[0, 1, 2, 3]],  # 5
]
# cctv insert
for i in range(n):
  data = list(map(int, input().split()))
  array.append(data)
  for j in range(m):
    if 1 <= data[j] <= 5:
      cctv.append([data[j], i, j])

answer = n * m  # 최소 사각지대
dfs(0, array)
print(answer)