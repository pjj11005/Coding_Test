import sys

input = sys.stdin.readline


def solution():
    for _ in range(int(input())):
        k, n = map(int, input().split())

        # 입력
        array = []
        for _ in range((n + 9) // 10):
            array.extend(map(int, input().split()))

        sorted_array = sorted(array)

        # 이동하지 않는 숫자들의 개수 카운트
        idx = 0
        for i in range(n):
            if array[i] == sorted_array[idx]:
                idx += 1

        print(k, n - idx)


if __name__ == "__main__":
    solution()
