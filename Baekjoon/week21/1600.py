import sys
from collections import deque

input = sys.stdin.readline


# BFS로 원숭이 최소 동작 횟수 구함
def bfs():
    visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
    visited[0][0][0] = 1
    q = deque([(0, 0, 0, 0)])  # x, y, cnt, use

    while q:
        x, y, cnt, use = q.popleft()
        if x == h - 1 and y == w - 1:  # 도달
            return cnt

        if use < k:  # 말의 움직임 사용
            for dx, dy in horse_move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny][use + 1] and array[nx][ny] == 0:
                    visited[nx][ny][use + 1] = 1
                    q.append((nx, ny, cnt + 1, use + 1))

        for dx, dy in move:  # 원숭이의 움직임
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny][use] and array[nx][ny] == 0:
                visited[nx][ny][use] = 1
                q.append((nx, ny, cnt + 1, use))

    return -1


k = int(input())
w, h = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(h)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 원숭이 움직임
horse_move = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]  # 말의 움직임
print(bfs())
