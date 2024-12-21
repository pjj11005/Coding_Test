import sys

input = sys.stdin.readline


def solution(d, s, array, clouds):
    # 구름 이동
    new_clouds = []
    visited = set()  # 구름 사라질 위치 저장
    dx, dy = move[d][0] * s, move[d][1] * s

    for x, y in clouds:
        nx, ny = (x + dx) % n, (y + dy) % n  # 범위 넘어 가는 것 고려
        visited.add((nx, ny))  # 구름 사라지는 곳 저장
        new_clouds.append((nx, ny))  # 이동한 구름 저장

    # 비 내림
    for x, y in new_clouds:
        array[x][y] += 1

    # 물복사버그
    for x, y in new_clouds:
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny]:
                array[x][y] += 1  # 물의 양 즐가

    # 새로운 구름 생김
    new_clouds = []
    for i in range(n):
        for j in range(n):
            if array[i][j] >= 2 and (i, j) not in visited:
                array[i][j] -= 2
                new_clouds.append((i, j))

    return array, new_clouds


n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]  # 바구니
clouds = [(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)]  # 구름의 좌표
move = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]  # 이동
direct = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # 대각선

for _ in range(m):
    d, s = map(int, input().split())
    array, clouds = solution(d, s, array, clouds)


print(sum(sum(a) for a in array))
