import sys

input = sys.stdin.readline


def solution():
    # DP : dp[n][k][last_bit]
    # n: 수열 길이, k: 인접한 비트 개수, last_bit: 마지막 비트(0 또는 1)
    dp = [[[0, 0] for _ in range(101)] for _ in range(101)]

    # 길이 1인 수열
    dp[1][0][0] = dp[1][0][1] = 1

    # DP 테이블 채우기
    for n in range(2, 101):
        for k in range(n):
            # 마지막 비트 0인 경우
            dp[n][k][0] = dp[n - 1][k][0] + dp[n - 1][k][1]

            # 마지막 비트 1인 경우
            dp[n][k][1] = dp[n - 1][k][0]  # 이전 비트 0이면 비트 증가 없음
            if k > 0:
                dp[n][k][1] += dp[n - 1][k - 1][1]  # 이전 비트 1이면 인접 비트 1증가

    for _ in range(int(input())):
        n, k = map(int, input().split())
        print(sum(dp[n][k]))


if __name__ == "__main__":
    solution()
