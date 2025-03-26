import sys

input = sys.stdin.readline


def solution():
    s = input().strip()
    n = len(s)
    dp = [[0] * 2 for _ in range(n)]  # dp[i][j] : i + 1번째 숫자까지 j + 1자리로 만들어진 수

    dp[0][0] = 1 if 0 < int(s[0]) < 10 else 0

    # 암호 해석 개수 구하기
    for i in range(1, n):
        # 한자리
        dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) if 0 < int(s[i]) < 10 else 0

        # 두자리
        dp[i][1] = dp[i - 1][0] if 10 <= int(s[i - 1] + s[i]) <= 26 else 0

    print(sum(dp[n - 1]) % 1000000)


if __name__ == "__main__":
    solution()
