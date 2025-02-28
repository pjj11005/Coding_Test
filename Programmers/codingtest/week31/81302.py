def check(x, y, place):
    # 상하좌우: 1
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            if place[nx][ny] == "P":
                return False

    # ㄱ모양: 2
    for dx, dy in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            if place[nx][ny] == "P" and (place[nx][y] == "O" or place[x][ny] == "O"):
                return False

    # 상하좌우: 2
    for dx, dy in ((-2, 0), (2, 0), (0, -2), (0, 2)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            if place[nx][ny] == "P" and place[(nx + x) // 2][(ny + y) // 2] == "O":
                return False

    return True


def solution(places):
    answer = []
    for place in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                # 안됨
                if place[i][j] == "P" and not check(i, j, place):
                    flag = 0
                    break

            # 안되는 경우 있음
            if flag == 0:
                break

        answer.append(flag)

    return answer
