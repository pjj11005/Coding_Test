import sys

input = sys.stdin.readline


def solution():
  n = int(input())

  if n < 100:
    print(n)
  else:
    answer = 99
    numbers = [str(i) for i in range(10, 100)]  # 두자리 한수 조합
    length = len(str(n))  # n의 자릿수

    # n의 자릿수까지 가능한 한수 계산
    for _ in range(3, length + 1):
      temp_numbers = []
      for num in numbers:
        x = (int(num[-1]) * 2) - int(num[-2])
        # 가능
        if 0 <= x <= 9 and int(num + str(x)) <= n:
          temp_numbers.append(num + str(x))
          answer += 1
      numbers = temp_numbers
      
    print(answer)


if __name__ == '__main__':
  solution()
