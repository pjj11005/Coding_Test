import sys
from itertools import combinations
input = sys.stdin.readline


def solution():
    # 배열을 반으로 나누기
    arr1 = arr[:n//2]
    arr2 = arr[n//2:]
    
    # 각 부분의 부분집합의 합 구하기
    sum1 = []
    sum2 = []
    
    for i in range(len(arr1) + 1):
        for comb in combinations(arr1, i):
            sum1.append(sum(comb))
    
    for i in range(len(arr2) + 1):
        for comb in combinations(arr2, i):
            sum2.append(sum(comb))
    
    # 이분탐색을 위해 정렬
    sum2.sort()
    
    answer = 0
    for s1 in sum1:
        if s1 > c:
            continue
    
        # 이분탐색
        start, end = 0, len(sum2)
        while start < end:
            mid = (start + end) // 2
            if sum2[mid] <= c - s1:
                start = mid + 1
            else:
                end = mid
    
        answer += end

    return answer
n, c = map(int, input().split())
arr = list(map(int, input().split()))
print(solution())