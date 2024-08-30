from itertools import permutations

def solution(numbers):
    answer = 0
    n = len(numbers)
    visited = []
    for i in range(1, n + 1):
        for comb in permutations(numbers, i):
            if comb[0] != 0:
                comb_num = int(''.join(list(comb)))
                if comb_num not in visited:
                    count = 0
                    for j in range(1, comb_num):
                        if comb_num % j == 0:
                            count += 1

                        if count >= 2:  # 소수 아님
                            break
                    if count == 1:  # 소수
                        answer += 1
                    visited.append(comb_num)
    return answer