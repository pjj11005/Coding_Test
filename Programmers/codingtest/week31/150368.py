'''내 풀이'''
# 사용자 별로 구입할 수 있는 이모티콘 구입
def purchase(percents, n, m, users, emoticons):
    result = [0, 0]
    for p, limit in users:
        total = 0
        for i in range(m):
            if p <= percents[i]:
                total += (emoticons[i] * (100 - percents[i])) / 100
        if total >= limit:
            result[0] += 1
        else:
            result[1] += total
    return result
                

def dfs(idx, percents, n, m, users, emoticons):
    global answer
    # 최대 이용자 및 판매액 갱신
    if idx == m:
        result = purchase(percents, n, m, users, emoticons)
        if result[0] > answer[0]:
            answer = result
        elif answer[0] == result[0] and result[1] > answer[1]:
            answer = result
        return
    
    for percent in [10, 20, 30, 40]:
        percents[idx] = percent
        dfs(idx + 1, percents, n, m, users, emoticons)

        
def solution(users, emoticons):
    global answer
    answer = [0, 0]
    n, m = len(users), len(emoticons)
    percents = [0] * m
    dfs(0, percents, n, m, users, emoticons)
    return answer


'''product 이용한 깔끔한 풀이'''
from itertools import product

def solution(users, emoticons):
    answer = [0, 0]  # [가입자 수, 판매액]
    discount_rates = [10, 20, 30, 40]
    
    # 모든 할인율 조합 탐색
    for rates in product(discount_rates, repeat=len(emoticons)):
        plus_users = 0
        total_sales = 0
        
        for user_rate, user_limit in users:
            user_purchase = 0
            
            # 사용자별 구매 계산
            for i, rate in enumerate(rates):
                if rate >= user_rate:  # 기준 할인율 이상이면 구매
                    user_purchase += emoticons[i] * (100 - rate) // 100
            
            # 구매 금액이 기준액 이상이면 플러스 가입, 아니면 판매액에 추가
            if user_purchase >= user_limit:
                plus_users += 1
            else:
                total_sales += user_purchase
        
        # 최적 결과 갱신 (가입자 우선, 판매액 차선)
        if plus_users > answer[0] or (plus_users == answer[0] and total_sales > answer[1]):
            answer = [plus_users, total_sales]
    
    return answer
