import sys

input = sys.stdin.readline


def solution():
  s = input().strip()
  stack = []
  result = ''

  # 후위 표기식 만들기
  for c in s:
    if c.isalpha():  # 문자(피연산자)
      result += c
    else:
      if c == '(':  # 여는 괄호
        stack.append(c)
      elif c in ('*', '/'):  # 곱셈, 나눗셈
        while stack and stack[-1] in ('*', '/'):
          result += stack.pop()
        stack.append(c)
      elif c in ('+', '-'):  # 덧셈, 뺄셈
        while stack and stack[-1] != '(':
          result += stack.pop()
        stack.append(c)
      else:  # 닫는 괄호
        while stack and stack[-1] != '(':
          result += stack.pop()
        stack.pop()  # '(' 제거

  # 남은 연산자 처리
  while stack:
    result += stack.pop()

  print(result)


if __name__ == '__main__':
  solution()
