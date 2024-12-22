# BFS + combinations : 116ms
import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline


def bfs(archers):
    global answer
    copyMap = [row[:] for row in board]  # 맵 복사
    killed = 0

    # 궁수가 위로 이동하는 형태로 구현
    for archer_row in range(n - 1, -1, -1):
        targets = set()  # 제거할 적의 위치

        # 각 궁수별로 가장 가까운 적 찾기
        for archer_col in archers:
            queue = deque([(archer_row, archer_col, 1)])
            visited = set()

            while queue:
                x, y, dist = queue.popleft()

                # 거리가 D를 초과하면 건너뛰기
                if dist > d:
                    continue

                # 적을 발견한 경우
                if copyMap[x][y] == 1:
                    targets.add((x, y))
                    break

                # 왼쪽, 위, 오른쪽 순서로 탐색
                for nx, ny in [(x, y - 1), (x - 1, y), (x, y + 1)]:
                    if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny, dist + 1))

        # 적 제거
        for tx, ty in targets:
            if copyMap[tx][ty] == 1:
                copyMap[tx][ty] = 0
                killed += 1

    answer = max(answer, killed)


n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# 가능한 모든 궁수 위치 조합에 대해 시뮬레이션
for archers in combinations(range(m), 3):
    bfs(archers)

print(answer)


""" DFS로 진행한 풀이 : 512ms
import sys

input = sys.stdin.readline


def play(archer):
    cnt = 0  # 제거하는 적의 수
    enemy = []  # 적의 좌표

    # 적의 좌표 담기
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1:
                enemy.append((i, j))

    while enemy:
        # 궁수 별로 가장 가까운 적 체크
        visited = set()
        for a, b in archer:
            sorted_enemy = sorted(enemy, key=lambda x: (abs(x[0] - a) + abs(x[1] - b), x[1]))
            for s_x, s_y in sorted_enemy:
                if abs(a - s_x) + abs(b - s_y) <= d:  # 가장 가까운 적 처치 가능
                    visited.add((s_x, s_y))
                    break
                else:  # 가장 가까운 적 처치 불가능
                    break

        # 적 처치 수 증가
        cnt += len(visited)

        # 살아남은 적들 한칸 내려오거나 다시 저장
        temp_enemy = []
        for x, y in enemy:
            if (x, y) in visited or x == n - 1:
                continue

            temp_enemy.append((x + 1, y))

        enemy = temp_enemy
    
    return cnt


def dfs(idx, archer):
    global answer
    if len(archer) == 3:
        answer = max(answer, play(archer))
        return

    for i in range(idx, m):
        dfs(i + 1, archer + [(n, i)])


n, m, d = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)] + [[0] * m]  # 격자판 + 궁수 배치 줄
answer = 0  # 답

dfs(0, [])
print(answer)
"""
