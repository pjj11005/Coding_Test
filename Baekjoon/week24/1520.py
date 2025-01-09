"""BFS + heapq"""

import sys
import heapq

input = sys.stdin.readline


# bfs
def bfs(m, n, array):
    dp = [[0] * n for _ in range(m)]  # 해당 위치에서 목적지 까지의 경로의 수 저장
    move = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q = [(-array[0][0], 0, 0)]
    dp[0][0] = 1

    while q:
        h, x, y = heapq.heappop(q)

        # 상하좌우 이동
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            # 이동 가능하면
            if 0 <= nx < m and 0 <= ny < n and array[nx][ny] < array[x][y]:
                if not dp[nx][ny]:  # 초기에만 진행 경로로 넣어주면 된다
                    heapq.heappush(q, (-array[nx][ny], nx, ny))
                dp[nx][ny] += dp[x][y]

    return dp[m - 1][n - 1]


def solution():
    m, n = map(int, input().split())  # 행, 열
    array = [list(map(int, input().split())) for _ in range(m)]  # 배열
    print(bfs(m, n, array))


if __name__ == "__main__":
    solution()

"""DFS + 메모이제이션
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# dfs
def dfs(x, y, m, n, array, dp):
    # 도달
    if x == m - 1 and y == n - 1:
        return 1

    # 이미 계산된 경로
    if dp[x][y] != -1:
        return dp[x][y]

    # 상하좌우 이동
    dp[x][y] = 0
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        # 이동 가능하면
        if 0 <= nx < m and 0 <= ny < n and array[nx][ny] < array[x][y]:
            dp[x][y] += dfs(nx, ny, m, n, array, dp)

    return dp[x][y]


def solution():
    m, n = map(int, input().split())  # 행, 열
    array = [list(map(int, input().split())) for _ in range(m)]  # 배열
    dp = [[-1] * n for _ in range(m)]  # 해당 위치에서 목적지 까지의 경로의 수 저장
    print(dfs(0, 0, m, n, array, dp))


if __name__ == "__main__":
    solution()
"""
