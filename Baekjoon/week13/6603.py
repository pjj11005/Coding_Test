import sys

input = sys.stdin.readline


def dfs(idx, array, k, s):
    # 6개 출력
    if len(array) == 6:
        print(*array)
        return

    # 백트래킹으로 선택
    for i in range(idx, k):
        if s[i] not in array:
            array.append(s[i])
            dfs(i + 1, array, k, s)
            array.pop()


def solution():
    while True:
        line = list(map(int, input().split()))

        # 종료
        if line[0] == 0:
            break

        # k, s
        k = line[0]
        s = line[1:]

        # 백트래킹 진행
        dfs(0, [], k, s)
        print()


if __name__ == "__main__":
    solution()
