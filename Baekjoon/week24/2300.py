"""PyPy3로만 맞음"""

import sys

input = sys.stdin.readline


def min_count(n, array):
    array.sort()  # x좌표 기준 정렬
    dp = [float("inf")] * (n + 1)  # dp
    dp[0] = 0

    # 통신폭 최소합 구하기
    for i in range(1, n + 1):
        max_height = 0
        for j in range(i, 0, -1):
            width = array[i - 1][0] - array[j - 1][0]  # 너비
            max_height = max(max_height, array[j - 1][1])  # 최대 y값
            square = max(width, max_height * 2)  # 너비와 높이 중 최대
            dp[i] = min(dp[i], dp[j - 1] + square)

    return dp[n]


def solution():
    n = int(input())
    array = []
    for _ in range(n):
        x, y = map(int, input().split())
        array.append((x, abs(y)))

    print(min_count(n, array))


if __name__ == "__main__":
    solution()
