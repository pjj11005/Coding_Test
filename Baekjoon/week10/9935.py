import sys
input = sys.stdin.readline

def solution(s, b):
  stack = [] # 문자를 저장할 스택
  for i in s:
    stack.append(i)
    if stack[len(stack) - len(b) : len(stack)] == b: # 뒤에서부터 폭발 문자열의 길이 만큼 비교
      for j in range(len(b)): # 같게 되면 스택에서 pop
        stack.pop()

  if not stack:
    return 'FRULA'
  else:
    return ''.join(stack)

s = list(input().strip())
b = list(input().strip())
print(solution(s, b))