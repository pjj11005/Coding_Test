def solution(money):
    n = len(money)
    dp1 = [0] * n # 첫번째에서 n - 2번째까지
    dp2 = [0] * n # 두번째에서 n - 1번까지
    dp1[0] = money[0]
    for i in range(1, n - 1):
        dp1[i] = max(dp1[i - 1], money[i] + dp1[i - 2])
    dp2[1] = money[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], money[i] + dp2[i - 2])
    return max(dp1[-2], dp2[-1])