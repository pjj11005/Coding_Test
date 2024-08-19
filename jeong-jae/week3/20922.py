import sys
input = sys.stdin.readline

def solution(n, k, array):
    visited = [[] for _ in range(100001)]
    dp = [0] * n
    start = 0
    for i in range(n):
        num = array[i]       
        if i == 0: # 처음
            visited[num].append(i) # 위치 저장
            dp[i] = 1
        else:
            length = len(visited[num])
            if length >= k:  # 수열 생성 불가능
                idx = visited[num][-k]
                if start > idx + 1:
                    dp[i] = dp[i - 1] + 1
                else:
                    start = idx + 1
                    dp[i] = i - start + 1
            else: # 수열 생성 가능
                dp[i] = dp[i - 1] + 1
            
            visited[num].append(i) # 위치 저장
    return max(dp)

n, k = map(int, input().split())
array = list(map(int, input().split()))
print(solution(n, k, array))