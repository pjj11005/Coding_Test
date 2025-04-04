import sys

input = sys.stdin.readline
INF = int(1e9)


def dfs(row, col, cnt):
    global ans, array, used_paper

    # 가지치기: 현재 카운트가 이미 찾은 최소값 이상이면 중단
    if cnt >= ans:
        return

    # 모든 행을 처리한 경우
    if row >= 10:
        ans = min(ans, cnt)
        return

    # 현재 행의 모든 열을 처리한 경우
    if col >= 10:
        dfs(row + 1, 0, cnt)
        return

    # 현재 위치가 0이면 다음 위치로 바로 이동
    if array[row][col] == 0:
        dfs(row, col + 1, cnt)
        return

    # 현재 위치가 1이면 가능한 모든 크기의 색종이 시도
    for size in range(1, 6):
        # 해당 크기 색종이를 모두 사용했거나 범위를 벗어나면 스킵
        if used_paper[size - 1] == 5 or row + size > 10 or col + size > 10:
            continue

        # 현재 위치에 size 크기의 색종이를 붙일 수 있는지 빠르게 확인
        can_attach = True
        for r in range(row, row + size):
            for c in range(col, col + size):
                if array[r][c] == 0:
                    can_attach = False
                    break
            if not can_attach:
                break

        if not can_attach:
            continue

        # 색종이 붙이기 (한 번에 처리)
        for r in range(row, row + size):
            for c in range(col, col + size):
                array[r][c] = 0

        used_paper[size - 1] += 1
        dfs(row, col + size, cnt + 1)  # 색종이 크기만큼 건너뛰기

        # 백트래킹
        used_paper[size - 1] -= 1
        for r in range(row, row + size):
            for c in range(col, col + size):
                array[r][c] = 1


def solution():
    global ans, array, used_paper
    array = [list(map(int, input().split())) for _ in range(10)]
    used_paper = [0] * 5
    ans = INF

    # 빈 보드인 경우 즉시 반환
    if not any(1 in row for row in array):
        return 0

    dfs(0, 0, 0)
    return ans if ans != INF else -1


if __name__ == "__main__":
    print(solution())
