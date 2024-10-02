import sys
input = sys.stdin.readline

def solution(n, d, k, c, array):
    answer = 0
    total_array = array + array[: k]
    for i in range(n):
        temp = total_array[i: i + k]
        if c in temp: # 쿠폰 음식 이미 먹음
            answer = max(answer, len(set(temp)))
        else:
            answer = max(answer, len(set(temp)) + 1)
    return answer

n, d, k, c = map(int, input().split())
array = [int(input()) for _ in range(n)]
print(solution(n, d, k, c, array))