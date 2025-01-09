import sys

input = sys.stdin.readline


def calculate(idx_set, n, array):
    total1 = total2 = 0  # 각 팀의 능력치
    idx_list2 = [i for i in range(n) if i not in idx_set]  # 링크
    idx_list = list(idx_set)  # 스타트

    # 스타트와 링크팀 점수 계산
    for i in range((n // 2) - 1):
        for j in range(i + 1, n // 2):
            i1, i2, i3, i4 = idx_list[i], idx_list[j], idx_list2[i], idx_list2[j]
            total1 += array[i1][i2] + array[i2][i1]
            total2 += array[i3][i4] + array[i4][i3]

    return abs(total1 - total2)


def dfs(idx, idx_set, n, array):
    global answer
    if len(idx_set) == (n // 2):  # 팀 결성
        result = calculate(idx_set, n, array)
        answer = min(answer, result)
        return

    # 선택하지 않은 인덱스 선택
    for i in range(idx, n):
        if i not in idx_set:
            dfs(i + 1, idx_set.union({i}), n, array)
    return


def main():
    global answer
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    answer = float("inf")
    dfs(0, {0}, n, array)
    print(answer)


if __name__ == "__main__":
    main()
