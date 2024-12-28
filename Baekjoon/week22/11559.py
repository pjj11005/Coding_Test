import sys
from collections import deque

input = sys.stdin.readline


def erase_fall(array, erase_list):
    # 연쇄 일어난 좌표들 빈칸으로
    for x, y in erase_list:
        array[x][y] = "."

    # 뿌요들 떨어짐
    for j in range(6):
        points = 11  # 떨어질 위치
        for i in range(11, -1, -1):
            if array[i][j] != ".":  # 뿌요 찾음
                array[points][j] = array[i][j]
                if points != i:
                    array[i][j] = "."
                points -= 1


# bfs로 뿌요뿌요 수행하는 함수
def bfs(i, j, array, visited):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([(i, j)])
    visited[i][j] = 1
    puyo_list = [(i, j)]
    color = array[i][j]

    while q:
        x, y = q.popleft()

        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and array[nx][ny] == color:
                visited[nx][ny] = 1
                q.append((nx, ny))
                puyo_list.append((nx, ny))

    return puyo_list


def main():
    array = [list(input().strip()) for _ in range(12)]
    answer = 0

    while True:
        visited = [[0] * 6 for _ in range(12)]
        is_possible = False  # 연쇄 유무
        erase_list = []  # 사라지는 좌표들

        for i in range(12):
            for j in range(6):
                if array[i][j] != "." and not visited[i][j]:  # 문자
                    puyo_list = bfs(i, j, array, visited)  # 같은 색의 블록 수
                    if len(puyo_list) >= 4:  # 연쇄 발생
                        is_possible = True
                        erase_list.extend(puyo_list)

        if is_possible:  # 연쇄 발생
            answer += 1
            erase_fall(array, erase_list)
        else:  # 연쇄 발생 안함
            break

    print(answer)


if __name__ == "__main__":
    main()
