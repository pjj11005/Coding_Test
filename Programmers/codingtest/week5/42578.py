def solution(clothes):
    answer = 1
    closet = {}
    for _, key in clothes:
        closet[key] = closet.get(key, 0) + 1  # key 없으면 0 아니면 해당 값

    for i in closet.values():
        answer *= i + 1  # 선택 안하는 경우 더해줌
    return answer - 1  # 모든 key 선택 안하는 경우 뺴줌
