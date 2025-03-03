def solution(sticker):
    n = len(sticker)

    if n == 1:
        return sticker[0]

    # 첫 번째 스티커 뜯는 경우
    dp1 = [0] * n  # 현재까지의 최대 점수
    dp1[0] = dp1[1] = sticker[0]
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    # 첫 번째 스티커 뜯지 않는 경우
    dp2 = [0] * n  # 현재까지의 최대 점수
    dp2[1] = sticker[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(dp1[-2], dp2[-1])
