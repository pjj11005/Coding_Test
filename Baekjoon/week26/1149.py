import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]

    for i in range(1, n):
        array[i][0] += min(array[i - 1][1], array[i - 1][2])  # R
        array[i][1] += min(array[i - 1][0], array[i - 1][2])  # G
        array[i][2] += min(array[i - 1][0], array[i - 1][1])  # B

    print(min(array[n - 1]))


if __name__ == "__main__":
    solution()
