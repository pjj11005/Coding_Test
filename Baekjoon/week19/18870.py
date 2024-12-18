import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(n, array):
    answer = [] # 답
    count = defaultdict(int) # 작은 수 개수
    set_array = sorted(set(array))

    # 작은 수 개수 저장
    for i in range(len(set_array)):
        count[set_array[i]] = i

    # 값 넣기
    for a in array:
        answer.append(count[a])

    print(*answer)

n = int(input())
array = list(map(int, input().split()))
solution(n, array)