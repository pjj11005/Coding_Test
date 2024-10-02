from itertools import permutations

def solution(k, dungeons):
    answer = 0
    num = k  # 초기 피로도
    for permutation in permutations(dungeons):
        count = 0  # 탐험 던전 수
        for a, b in list(permutation):
            if k >= a:  # 던전 탐험 가능
                k -= b
                count += 1
            else:
                break
        answer = max(answer, count)
        k = num
    return answer