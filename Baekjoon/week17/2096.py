import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    a, b, c = map(int, input().split())  # 최솟값
    d, e, f = a, b, c  # 최댓값

    # 최대, 최소 구하기
    for i in range(1, n):
        a2, b2, c2 = map(int, input().split())  # 새로운 최솟값
        d2, e2, f2 = a2, b2, c2  # 새로운 최댓값

        # 최소
        a2 += min(a, b)
        b2 += min(a, b, c)
        c2 += min(b, c)
        a, b, c = a2, b2, c2

        # 최대
        d2 += max(d, e)
        e2 += max(d, e, f)
        f2 += max(e, f)
        d, e, f = d2, e2, f2

    print(max(d, e, f), min(a, b, c))


if __name__ == "__main__":
    solution()
