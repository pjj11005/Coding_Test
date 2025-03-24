import sys

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    answer = 0

    start, end = 0, 10000
    while start <= end:
        mid = (start + end) // 2
        count = 1  # 구간의 수
        min_value, max_value = 10000, 0
        for i in range(n):
            min_value = min(min_value, array[i])
            max_value = max(max_value, array[i])
            if max_value - min_value > mid:
                count += 1
                min_value = max_value = array[i]

        # 값 증가
        if count > m:
            start = mid + 1
        # 값 감소
        else:
            answer = mid
            end = mid - 1

    print(answer)


if __name__ == "__main__":
    solution()
