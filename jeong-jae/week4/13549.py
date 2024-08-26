import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)


def solution(n, k):
  check = [INF] * 100001
  q = deque([(n, 0)])
  check[n] = 0

  while q:
    now, time = q.popleft()
    if now == k:
      break
    for i in [-1, 1, 2]:
      if i == 2:
        next = now * 2
        if 0 <= next <= 100000 and check[next] > time:  # 좌표 위
          check[next] = time
          q.append((next, time))
      else:
        next = now + i
        if 0 <= next <= 100000 and check[next] > time + 1:  # 좌표 위
          check[next] = time + 1
          q.append((next, time + 1))

  return check[k]


n, k = map(int, input().split())
print(solution(n, k))

'''
- 현재 지점에서 앞, 뒤, 2배 위치 3가지 방식으로 진행 가능
- 각 방식 별로 (위치, 시간)으로 BFS 탐색을 사용하여 문제 해결
'''