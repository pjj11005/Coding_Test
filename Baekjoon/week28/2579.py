import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    array = [0] + [int(input()) for _ in range(n)]

    if n == 1:
        print(array[1])
    elif n == 2:
        print(array[1] + array[2])
    else:
        dp = [0] * (n + 1)
        dp[1] = array[1]
        dp[2] = array[1] + array[2]
        dp[3] = max(array[1] + array[3], array[2] + array[3])
        
        # 점화식 이용하여 계산
        for i in range(4, n + 1):
            dp[i] = max(dp[i - 3] + array[i - 1], dp[i - 2]) + array[i]
        
        print(dp[n])

if __name__ == '__main__':
    solution()
