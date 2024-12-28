import sys

input = sys.stdin.readline


def check(n, m, array):
    for i in range(n):
        for j in range(m):
            if array[i][j] == ".":
                return False
    return True


def go(x, y, dx, dy, n, m, array):
    while True:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == ".":
            array[nx][ny] = "*"
        else:
            return x, y
        x, y = nx, ny


def back(x, y, nx, ny, dx, dy, array):
    while True:
        array[nx][ny] = "."
        nx -= dx
        ny -= dy

        if nx == x and ny == y:
            return


def dfs(cnt, x, y, n, m, array):
    global answer  # answer를 전역 변수로 선언
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = go(x, y, dx, dy, n, m, array)  # 진행
        if nx == x and ny == y:  # 안변함
            continue
        dfs(cnt + 1, nx, ny, n, m, array)
        back(x, y, nx, ny, dx, dy, array)  # 다시 돌아감

    if check(n, m, array):  # 모든 점을 방문한 경우
        answer = min(answer, cnt)
        return


def main():
    global answer  # answer를 전역 변수로 선언
    case_count = 1

    while True:
        # 입력 읽기
        line = input().strip()
        if not line:  # EOF 처리
            break

        n, m = map(int, line.split())
        array = [list(input().strip()) for _ in range(n)]
        answer = float("inf")  # 무한대로 초기화

        for i in range(n):
            for j in range(m):
                if array[i][j] == ".":
                    array[i][j] = "*"
                    dfs(0, i, j, n, m, array)
                    array[i][j] = "."

        if answer == float("inf"):  # 경우가 없으면 -1 출력
            print(f"Case {case_count}: -1")
        else:
            print(f"Case {case_count}: {answer}")

        case_count += 1


if __name__ == "__main__":
    main()
