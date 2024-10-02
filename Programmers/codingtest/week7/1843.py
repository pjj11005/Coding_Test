def solution(arr):
    nums = [int(x) for x in arr[::2]]
    ops = arr[1::2]
    n = len(nums)
    
    # dp[i][j]는 i부터 j까지의 부분 표현식의 최소값과 최대값을 저장
    dp = [[(float('inf'), float('-inf')) for _ in range(n)] for _ in range(n)]
    
    # 초기화: 단일 숫자에 대한 최소값과 최대값은 숫자 자체
    for i in range(n):
        dp[i][i] = (nums[i], nums[i])
    
    # 길이가 2 이상인 부분 표현식에 대해 계산
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                op = ops[k]
                left_min, left_max = dp[i][k]
                right_min, right_max = dp[k+1][j]
                
                if op == '+':
                    dp[i][j] = (
                        min(dp[i][j][0], left_min + right_min),
                        max(dp[i][j][1], left_max + right_max)
                    )
                else:  # op == '-'
                    dp[i][j] = (
                        min(dp[i][j][0], left_min - right_max),
                        max(dp[i][j][1], left_max - right_min)
                    )
    
    # 전체 표현식의 최대값 반환
    return dp[0][n-1][1]