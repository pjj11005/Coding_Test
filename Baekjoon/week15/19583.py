import sys
from collections import defaultdict
input = sys.stdin.readline

# 분 단위로 변환
def to_minutes(timestamp):
  m, s = map(int, timestamp.split(':'))
  return m * 60 + s

def solution():
  s, e, q = input().strip().split()
  s, e, q = to_minutes(s), to_minutes(e), to_minutes(q)
  answer = 0
  count = defaultdict(int) # 채팅 횟수
  while True:
    line = input().strip()
    if not line: # 입력 끝
      break
    timestamp, name = line.split()
    timestamp = to_minutes(timestamp)
    if 0 <= timestamp <= s and count[name] == 0: # 개강총회를 시작하기 전
      count[name] += 1
    elif e <= timestamp <= q and count[name] == 1: # 개강총회를 끝내고 나서, 스트리밍을 끝낼 때까지
      count[name] += 1
      answer += 1
  return answer
print(solution())