import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    
    if n == 1: # 1
        print(3 % 9901)
    elif n == 2: # 2
        print(7 % 9901)
    else: # 3 이상
        dp = [0] * (n + 1)
        dp[1], dp[2] = 3, 7
        for i in range(3, n + 1):
            dp[i] = (2 * (dp[i - 1]) + dp[i - 2]) % 9901
        
        print(dp[n])

if __name__ == "__main__":
    solution()