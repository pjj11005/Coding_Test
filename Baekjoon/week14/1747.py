import sys
input = sys.stdin.readline

def is_prime(x):
  if x <= 1: # 1
    return False
  if x <= 3: # 2, 3
    return True
  if x % 2 == 0 or x % 3 == 0: # 짝수, 3의 배수
    return False
  i = 5
  while i * i <= x: # 6k + 1, 6k - 1은 소수(2, 3 제외)
    if x % i == 0 or x % (i + 2) == 0:
      return False
    i += 6
  return True
  
def solution(n):
  while True:
    if is_prime(n) and str(n) == str(n)[::-1]:
      return n
    n += 1
  
n = int(input())
print(solution(n))