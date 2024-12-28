# 큐를 두개 이용하며 풀이
import sys
from collections import deque

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    time = -1  # 시간
    prev = cnt = 0  # 이전에 남아 있는 치즈, 녹은 치즈 수

    q = deque([(0, 0)])
    array[0][0] = -1

    while q:
        next_q = deque()  # 다음에 녹을 치즈 위치 저장할 큐
        prev = cnt  # 이전 반복에서 녹은 치즈 수 저장 -> 결국 마지막에 이전에 녹은 수가 1시간 전에 남은 치즈의 수가 됨
        cnt = 0

        while q:
            x, y = q.popleft()

            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if array[nx][ny] == 0:  # 공기
                        q.append((nx, ny))
                    elif array[nx][ny] == 1:  # 외부 공기와 닿은 치즈
                        next_q.append((nx, ny))
                        cnt += 1

                    array[nx][ny] = -1  # 방문 처리

        # 다음에 녹을 치즈 위치로 업데이트
        q = next_q
        time += 1

    print(time)
    print(prev)


if __name__ == "__main__":
    main()


""" 내 풀이 : 64ms -> 각 단계를 쪼개서 구현
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
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if array[nx][ny] == 2:  # 외부 공기랑 닿음
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
    count = 0  # 남아 있는 치즈

    make_outside_air(n, m, array)  # 외부 공기 체크(외부 공기 칸은 2로 바꿈)
    cheese = find_cheese(n, m, array)  # 치즈 좌표 저장

    while True:
        # 이전 치즈 개수 저장
        count = len(cheese)

        check_outside_air(n, m, array)  # 내부 공기 -> 외부 공기

        # 치즈 녹이기
        cheese = erase_cheese(array, cheese)
        time += 1

        # 남은 치즈 없음
        if not cheese:
            print(time)
            print(count)
            break


if __name__ == "__main__":
    main()
"""
