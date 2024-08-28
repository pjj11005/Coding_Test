import sys
from collections import deque

input = sys.stdin.readline

def solution(n, k, array):
  count = 0  # 내구도 0의 갯수
  time = 0  # 단계
  q = deque()  # 내구도, 로봇 유무
  for a in array:
    q.append([a, 0])

  while True:
    # 1단계
    x = q.pop()
    q.appendleft(x)
    q[n - 1][1] = 0 # 내리는 위치 -> 내리기

    # 2단계
    for i in range(n - 1, -1, -1):
      if q[i][1] == 1 and q[i + 1][0] > 0 and q[i + 1][1] == 0:  # 로봇 이동 가능
        q[i][1], q[i + 1][1] = 0, 1
        q[i + 1][0] -= 1
        if q[i + 1][0] == 0:  # 0 count
          count += 1

        if i + 1 == n - 1:  # 내리는 위치 -> 내리기 가능
          q[n - 1][1] = 0

    # 3단계
    if q[0][0] > 0:  # 올리기 가능
      q[0][0] -= 1
      q[0][1] = 1
      if q[0][0] == 0:  # 0 count
        count += 1

    # 4단계
    time += 1
    # print(time, q, count)
    if count >= k:
      return time

n, k = map(int, input().split())
array = list(map(int, input().split()))
print(solution(n, k, array))

'''
- 내리기라는 것은 로봇 자체를 컨베이어 벨트에서 내리는 것을 의미했다
'''