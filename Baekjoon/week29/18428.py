import sys
from itertools import combinations

input = sys.stdin.readline


def watch(x, y, n, direction, array):
  if direction == 0:  # 왼쪽
    while y >= 0:
      if array[x][y] == 'S':
        return True
      if array[x][y] == 'O':
        return False
      y -= 1
  if direction == 1:  # 위쪽
    while x >= 0:
      if array[x][y] == 'S':
        return True
      if array[x][y] == 'O':
        return False
      x -= 1
  if direction == 2:  # 오른쪽
    while y < n:
      if array[x][y] == 'S':
        return True
      if array[x][y] == 'O':
        return False
      y += 1
  if direction == 3:  # 아래쪽
    while x < n:
      if array[x][y] == 'S':
        return True
      if array[x][y] == 'O':
        return False
      x += 1
  return False


def process(n, array, teachers):
  for x, y in teachers:
    for i in range(4):
      if watch(x, y, n, i, array):
        return True
  return False


def solution():
  n = int(input())
  array = [list(input().split()) for _ in range(n)]
  spaces, teachers = [], []
  find = False  # 학생들이 감시당하지 않고 벽 설치 가능한지

  # T, 빈칸 좌표 저장
  for i in range(n):
    for j in range(n):
      if array[i][j] == 'T':
        teachers.append((i, j))
      elif array[i][j] == 'X':
        spaces.append((i, j))

  # 각 장애물 설치 경우에 따라 판단
  for data in combinations(spaces, 3):
    for x, y in data:  # 벽 설치
      array[x][y] = 'O'

    if not process(n, array, teachers):
      find = True
      break

    for x, y in data:
      array[x][y] = 'X'

  if find:
    print('YES')
  else:
    print('NO')


if __name__ == '__main__':
  solution()
