import sys
input = sys.stdin.readline

def solution(n):
  # n이 처리되었는지 확인
  if n in memo: 
    return memo[n]
  # 0일 때
  if n == 0:
    return 1
  # 저장
  memo[n] = solution(n // p) + solution(n // q)
  return memo[n]
  
n, p, q = map(int, input().split())
memo = {}
print(solution(n))