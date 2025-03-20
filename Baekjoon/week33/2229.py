import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    array = list(map(int, input().split()))
    dp = [0] * (n + 1)  # dp[i] : i명번째 학생까지 조를 짰을 때 최댓값

    for i in range(n):
        dp[i + 1] = dp[i]  # 현재 학생 포함하지 않는 경우(이전까지 최적해)
        min_val = max_val = array[i]  # 현재 학생만으로 새 조 시작
        j = i - 1

        # 최댓값이나 최솟값이 갱신될 때만 새로운 조합 확인
        while j >= 0 and (array[j] < min_val or array[j] > max_val):
            min_val = min(min_val, array[j])
            max_val = max(max_val, array[j])
            dp[i + 1] = max(dp[i + 1], dp[j] + max_val - min_val)
            j -= 1

    print(dp[n])


if __name__ == "__main__":
    solution()
