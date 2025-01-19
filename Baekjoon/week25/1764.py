import sys

input = sys.stdin.readline


def solution():
  n, m = map(int, input().split())
  words = set()  # 듣도 못한 사람의 명단
  answer = []  # 듣보잡

  # 듣고 못한 명단 추가
  for _ in range(n):
    words.add(input().strip())

  # 듣보잡 찾기
  for _ in range(m):
    word = input().strip()
    if word in words:
      answer.append(word)

  # 듣보잡 출력
  print(len(answer))
  for word in sorted(answer):
    print(word)


if __name__ == '__main__':
  solution()
