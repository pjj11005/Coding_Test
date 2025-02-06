import sys

input = sys.stdin.readline

def solution():
    for _ in range(int(input())):
    	n = int(input())
    	if n == 1:
    		print(1)
    	elif n == 2:
    		print(2)
    	else:
    		dp = [0] * 12
    		dp[1], dp[2], dp[3] = 1, 2, 4
    		
    		# 점화식으로 dp 계산
    		for i in range(4, n + 1):
    			dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    		
    		print(dp[n])

if __name__ == '__main__':
    solution()
