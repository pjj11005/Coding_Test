import sys

input = sys.stdin.readline


def set_dice(n, dices, pairs):
    global answer

    for i in range(6):
        num = dices[0][i]  # 1번 주사위 윗면의 숫자
        total = max(dices[0][x] for x in pairs[i][1])
        # 2번 부터 최대값 더하기
        for j in range(1, n):
            idx = dices[j].index(num)
            total += max(dices[j][x] for x in pairs[idx][1])
            num = dices[j][pairs[idx][0]]
        answer = max(answer, total)


def solution():
    global answer
    n = int(input())
    dices = [list(map(int, input().split())) for _ in range(n)]
    pairs = [
        [5, [1, 2, 3, 4]],
        [3, [0, 2, 4, 5]],
        [4, [0, 1, 3, 5]],
        [1, [0, 2, 4, 5]],
        [2, [0, 1, 3, 5]],
        [0, [1, 2, 3, 4]],
    ]  # 짝
    answer = 0

    set_dice(n, dices, pairs)
    print(answer)


if __name__ == "__main__":
    solution()
