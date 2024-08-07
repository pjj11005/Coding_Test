import sys
input = sys.stdin.readline

def solution(x, y):
  if x % (y + 1) == 0:
    return x // (y + 1)
  else:
    return (x // (y + 1)) + 1

h, w, n, m = map(int, input().split())
print(solution(h, n) * solution(w, m))