import sys
from collections import defaultdict

input = sys.stdin.readline

def memoization(sub, d, prev, idx):
    # 해당 합의 개수 증가
    d[prev] += 1
    
    # 부분 수열 만들며 진행
    for i in range(idx, len(sub)):
        nxt = prev + sub[i]
        memoization(sub, d, nxt, i + 1)

def solution():
    n, s = map(int, input().split())
    array = list(map(int, input().split()))
    
    # 수열 분할
    left, right = defaultdict(int), defaultdict(int) 
    m = n // 2
    
    # 분할해서 부분 수열 합의 개수 구함
    memoization(array[:m], left, 0, 0)
    memoization(array[m:], right, 0, 0)
    
    # 합이 s가 되는 조합 수 구함
    answer = sum(left[l] * right[s - l] for l in left if s - l in right)
    print(answer if s else answer - 1) # s=0일 때 공집합 + 공집합 조합 제외

if __name__ == '__main__':
    solution()
