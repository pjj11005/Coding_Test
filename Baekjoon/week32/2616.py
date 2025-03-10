import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    array = [0] + list(map(int, input().split()))
    m = int(input())

    # 누적합 계산
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + array[i]

    # dp[i][j]: i번째 소형기관차까지 사용했고, j번째 객차까지 고려했을 때의 최대 승객 수
    dp = [[0] * (n + 1) for _ in range(4)]

    for i in range(1, 4):
        for j in range(i * m, n + 1):
            # 현재 객차 선택 안함
            dp[i][j] = dp[i][j - 1]

            # 현재 객차 부터 m개 선택
            # 현재 구간의 합: prefix_sum[j] - prefix_sum[j - m]
            dp[i][j] = max(dp[i][j], dp[i - 1][j - m] + (prefix_sum[j] - prefix_sum[j - m]))

    print(dp[3][n])


if __name__ == "__main__":
    solution()
