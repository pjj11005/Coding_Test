import sys
from collections import defaultdict

input = sys.stdin.readline


# find 함수
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


# union 함수
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


def solution():
  n = int(input())
  m = int(input())
  parent = list(range(n + 1))
  enemy = [0] * (n + 1)

  # 원수, 친구 저장
  for _ in range(m):
    info, a, b = input().split()
    a, b = int(a), int(b)
    # 원수
    if info == 'E':
      if enemy[a]:
        union_parent(parent, enemy[a], b)
      enemy[a] = b
      if enemy[b]:
        union_parent(parent, enemy[b], a)
      enemy[b] = a
    # 친구
    else:
      union_parent(parent, a, b)

  # 마지막으로 같은 팀 갱신
  for i in range(1, n + 1):
    find_parent(parent, i)

  print(len(set(parent[1:])))


if __name__ == '__main__':
  solution()
