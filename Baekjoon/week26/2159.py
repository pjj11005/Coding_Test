import sys

input = sys.stdin.readline
INF = float("inf")


def solution():
    n = int(input())
    sx, sy = map(int, input().split())
    points = [list(map(int, input().split())) for _ in range(n)]
    move = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))
    # dp[i][j]: i번째 주문을 j방향에서 처리했을 때의 최소 거리
    dp = [[INF] * 5 for _ in range(n)]

    # 첫번째 주문 처리
    for i, (dx, dy) in enumerate(move):
        nx, ny = points[0][0] + dx, points[0][1] + dy
        dp[0][i] = abs(nx - sx) + abs(ny - sy)

    # 나머지 주문 처리
    for i in range(1, n):
        for k in range(5):  # 현재 위치의 가능한 5가지 점
            x, y = points[i][0] + move[k][0], points[i][1] + move[k][1]
            for j in range(5):  # 이전 위치의 가능한 5가지 점
                px, py = points[i - 1][0] + move[j][0], points[i - 1][1] + move[j][1]
                dp[i][k] = min(dp[i][k], dp[i - 1][j] + abs(px - x) + abs(py - y))

    print(min(dp[n - 1]))


if __name__ == "__main__":
    solution()
