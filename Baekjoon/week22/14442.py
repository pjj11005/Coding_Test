import sys
from collections import deque

input = sys.stdin.readline


# BFS 탐색 함수
def bfs(n, m, k, array):
    answer = -1
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
    q = deque([(0, 0, 0, 1)])  # x, y, cnt, dist
    visited[0][0][0] = 1

    while q:
        x, y, cnt, dist = q.popleft()

        if x == n - 1 and y == m - 1:
            answer = dist
            break

        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:  # 범위 내
                if array[nx][ny] == 1 and cnt < k and not visited[nx][ny][cnt + 1]:  # 벽 부수기 가능
                    visited[nx][ny][cnt + 1] = 1
                    q.append((nx, ny, cnt + 1, dist + 1))
                elif array[nx][ny] == 0 and not visited[nx][ny][cnt]:  # 그냥 진행 가능
                    visited[nx][ny][cnt] = 1
                    q.append((nx, ny, cnt, dist + 1))

    return answer


def main():
    n, m, k = map(int, input().split())
    array = [list(map(int, input().strip())) for _ in range(n)]
    print(bfs(n, m, k, array))


if __name__ == "__main__":
    main()
