import sys

input = sys.stdin.readline


def put_book_back(m, minus, plus):
  answer = []  # 답

  # 내림 차순 정렬
  minus.sort(reverse=True)
  plus.sort(reverse=True)

  # m개씩 건너뛰며 각 그룹의 최대값 저장
  for i in minus[::m]:
    answer.append(i)

  # m개씩 건너뛰며 각 그룹의 최대값 저장
  for i in plus[::m]:
    answer.append(i)

  # 왕복을 해야하므로 총합 X 2를 하고 가장 긴 거리를 마지막에 하면 됨
  return 2 * sum(answer) - max(answer)


def solution():
  n, m = map(int, input().split())
  array = list(map(int, input().split()))

  # 책 음수 양수 포인트 나눠서 담기(절대값으로)
  minus, plus = [], []
  for a in array:
    if a < 0:
      minus.append(-a)
    else:
      plus.append(a)

  print(put_book_back(m, minus, plus))


if __name__ == '__main__':
  solution()
