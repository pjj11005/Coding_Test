import sys
from collections import deque

input = sys.stdin.readline


def bfs(i, j, n, m, array, move, visited, melt):
    q = deque([(i, j)])
    visited[i][j] = 1
    while q:
        x, y = q.popleft()

        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if array[nx][ny] == 0:  # 빈 공간
                melt[x][y] += 1
            elif array[nx][ny] != 0 and not visited[nx][ny]:  # 같은 덩어리
                visited[nx][ny] = 1
                q.append((nx, ny))


def solution():
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    move = ((-1, 0), (1, 0), (0, -1), (0, 1))

    # 빙산 녹이기
    time = 0
    while True:
        visited = [[0] * m for _ in range(n)]  # 방문 배열
        melt = [[0] * m for _ in range(n)]  # 녹는 높이
        count = 0  # 덩어리 개수

        # 빙산 덩어리 계산
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if not visited[i][j] and array[i][j] > 0:
                    bfs(i, j, n, m, array, move, visited, melt)
                    count += 1

        # 두덩어리 이상 분리
        if count >= 2:
            print(time)
            break

        # 분리 안됨
        if count == 0:
            print(0)
            break

        # 녹이기
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                array[i][j] = max(0, array[i][j] - melt[i][j])

        time += 1


if __name__ == "__main__":
    solution()
