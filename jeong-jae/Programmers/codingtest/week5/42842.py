def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, yellow + 1):
        if yellow % i == 0:  # 노란색 만드는 경우
            a = max(i + 2, (yellow // i) + 2)  # 카펫 가로
            b = min(i + 2, (yellow // i) + 2)  # 카펫 세로
            if a * b == total:  # 카펫 가능
                answer = [a, b]
                break
    return answer
