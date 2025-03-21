import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]  # dp[i][j] : i ~ j 번째 행렬 곱의 최솟값

    # 대각선 방향으로 dp 테이블 채우기 : 간격을 늘려가며 해당 구간들 채우기 -> 대각선 모양으로 채워짐
    for diagonal in range(1, n):  # 대각선 간격
        for i in range(n - diagonal):  # 시작 행렬
            j = i + diagonal  # 끝 행렬

            # 초기값 최대
            dp[i][j] = (2**31) - 1

            # k를 기준으로 분할하여 최소 연산 횟수 계산
            for k in range(i, j):
                # (i~k 행렬 연산) + (k+1~j 행렬 연산) + (두 행렬 곱셈 연산: 앞의 두 괄호 연산)
                cost = dp[i][k] + dp[k + 1][j] + array[i][0] * array[k][1] * array[j][1]
                dp[i][j] = min(dp[i][j], cost)

    print(dp[0][n - 1])


if __name__ == "__main__":
    solution()
