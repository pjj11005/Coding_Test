import sys
from collections import deque

input = sys.stdin.readline


# 내부 공기 외부 공기로 바꾸는 함수
def check_outside_air(n, m, array):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                is_valid = False
                for di, dj in move:
                    ni, nj = i + di, j + dj
                    if array[ni][nj] == 2:  # 외부 공기와 접촉
                        is_valid = True
                        break

                # 내부 공기 -> 외부 공기로
                if is_valid:
                    q = deque([(i, j)])
                    visited[i][j] = 1
                    array[i][j] = 2
                    while q:
                        x, y = q.popleft()

                        for dx, dy in move:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and array[nx][ny] == 0:
                                visited[nx][ny] = 1
                                array[nx][ny] = 2
                                q.append((nx, ny))


# 초기에 외부 공기 변환하는 함수
def make_outside_air(n, m, array):
    visited = [[0] * m for _ in range(n)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([(0, 0)])
    visited[0][0] = 1
    array[0][0] = 2

    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and array[nx][ny] == 0:
                visited[nx][ny] = 1
                array[nx][ny] = 2
                q.append((nx, ny))


# 치즈 녹이는 함수
def erase_cheese(array, cheese):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 녹는 치즈 찾기
    for x, y in cheese:
        cnt = 0
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if array[nx][ny] == 2:  # 외부 공기랑 닿음
                cnt += 1

            if cnt == 2:
                array[x][y] = -1  # 녹은 표시
                break

    # 녹는 치즈 녹이기 + 남은 치즈 저장
    new_cheese = []
    for x, y in cheese:
        if array[x][y] == -1:  # 녹게되는 치즈
            array[x][y] = 2
        elif array[x][y] == 1:  # 안녹은 치즈
            new_cheese.append((x, y))

    return new_cheese


# 초기 치즈 좌표 찾는 함수
def find_cheese(n, m, array):
    cheese = []
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1:  # 치즈
                cheese.append((i, j))

    return cheese


def main():
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    time = 0  # 시간

    make_outside_air(n, m, array)  # 외부 공기 체크(외부 공기 칸은 2로 바꿈)
    cheese = find_cheese(n, m, array)  # 치즈 좌표 저장

    while True:
        check_outside_air(n, m, array)  # 내부 공기 -> 외부 공기

        # 치즈 녹이기
        cheese = erase_cheese(array, cheese)
        time += 1

        # 남은 치즈 없음
        if not cheese:
            print(time)
            break


if __name__ == "__main__":
    main()
