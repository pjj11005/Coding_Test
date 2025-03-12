import sys

input = sys.stdin.readline


def solution():
    for _ in range(int(input())):
        n, m = map(int, input().split())

        # mCn
        a, b = m, n
        for i in range(n - 1):
            m -= 1
            n -= 1
            a *= m
            b *= n

        print(a // b)


def solution2():
    dp = [[0] * 30 for _ in range(30)]
    # iC1
    for i in range(1, 30):
        dp[1][i] = i

    # dp(콤비네이션 성질 이용) 계산
    for i in range(2, 30):
        for j in range(i, 30):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

    for _ in range(int(input())):
        n, m = map(int, input().split())
        print(dp[n][m])


if __name__ == "__main__":
    solution2()
