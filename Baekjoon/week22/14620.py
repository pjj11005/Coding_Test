import sys

input = sys.stdin.readline


# 꽃 심기 가능 확인 함수
def check(x, y, n, visited):
    for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if visited[nx][ny]:
            return False
    return True


# 꽃 심는 비용 계산 함수
def get_score(x, y, n, array):
    flower_sum = 0
    for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        flower_sum += array[nx][ny]
    return flower_sum


# dfs로 꽃 심는 함수
def dfs(cnt, total, n, array, visited):
    global answer
    if cnt == 3:
        answer = min(answer, total)
        return

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if check(i, j, n, visited):
                # 방문 표시
                for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = i + dx, j + dy
                    visited[nx][ny] = 1

                # 다음 단계로 재귀 호출
                dfs(cnt + 1, total + get_score(i, j, n, array), n, array, visited)

                # 방문 해제
                for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = i + dx, j + dy
                    visited[nx][ny] = 0


def main():
    global answer
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    answer = float("inf")
    dfs(0, 0, n, array, visited)
    print(answer)


if __name__ == "__main__":
    main()
