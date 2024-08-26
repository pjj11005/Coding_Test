import sys
input = sys.stdin.readline

t = int(input())

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])

'''
- 모든 수는 1만으로 이루어진 합을 1개씩 가진다
- 그 후, n-2번째 경우에서 각각 2를 더하는 경우로 갱신해준다
- 마지막으로, 1과2의 합으로 이루어진 경우에 3을 더하는 경우로 갱신한다
'''