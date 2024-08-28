import sys
input = sys.stdin.readline

def test1(p):  # 조건 1
  for i in p:
    if i in ['a', 'e', 'i', 'o', 'u']:
      return True
  return False

def test2(p):  # 조건 2
  vo = ['a', 'e', 'i', 'o', 'u']
  for i in range(len(p) - 2):
    if (p[i] in vo) and (p[i + 1] in vo) and (p[i + 2] in vo):  # 모음 연속
      return False
    elif (p[i] not in vo) and (p[i + 1] not in vo) and (p[i + 2] not in vo):  # 자음 연속
      return False
  return True

def test3(p):  # 조건 3
  for i in range(len(p) - 1):
    if p[i] == p[i + 1] and p[i] != 'e' and p[i] != 'o':
      return False
  return True

while True:
  p = input().strip()
  if p == 'end':  # 종료
    break

  if test1(p) and test2(p) and test3(p):  # acceptable
    print(f'<{p}> is acceptable.')
  else:  # not acceptable
    print(f'<{p}> is not acceptable.')
