import sys
from itertools import combinations

input = sys.stdin.readline


def dfs(game_idx, games, scores):
    global result
    # 모든 경기 종료 -> 가능
    if game_idx == 15:
        if all(sum(team) == 0 for team in scores):
            result = 1
        return

    team1, team2 = games[game_idx]

    # 승, 패, 무승부 가능한 경우 탐색
    for t1, t2 in ((0, 2), (1, 1), (2, 0)):
        if scores[team1][t1] and scores[team2][t2]:
            scores[team1][t1] -= 1
            scores[team2][t2] -= 1
            dfs(game_idx + 1, games, scores)
            scores[team1][t1] += 1
            scores[team2][t2] += 1

    return


def solution():
    global result
    results = []
    games = list(combinations(range(6), 2))  # 모든 대진 조합

    for _ in range(4):
        result = 0
        array = list(map(int, input().split()))

        # 6개국 결과 저장
        scores = [array[i : i + 3] for i in range(0, 16, 3)]

        dfs(0, games, scores)

        results.append(result)

    print(*results)


if __name__ == "__main__":
    solution()
