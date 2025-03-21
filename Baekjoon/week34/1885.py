import sys

input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())
    sequence = [int(input()) for _ in range(n)]

    cnt = 0  # 구간의 개수
    check = set()  # 현재 구간에 포함된 숫자들

    for num in sequence:
        if 1 <= num <= k:
            check.add(num)

        if len(check) == k:  # 모든 숫자(1~k)가 모였다면
            cnt += 1
            check = set()  # 새로운 구간 시작

    print(cnt + 1)


if __name__ == "__main__":
    solution()
