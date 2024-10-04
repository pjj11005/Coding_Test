import sys
input = sys.stdin.readline

def solution(n, array):
    num = list(range(1, n + 1))
    answer = [] # 정답
    
    for i in range(n - 1, -1, -1): # 큰 수부터 자신 보다 큰 요소들 개수의 다음 위치에 삽입
        answer.insert(array[i], num[i])
    
    for a in answer:
        print(a, end=' ')

n = int(input())
array = list(map(int, input().split()))
solution(n, array)

''' 순열로 푼 풀이
import sys
from itertools import permutations
input = sys.stdin.readline

def solution(n, array):
    for perm in permutations(range(1, n + 1), n): # 키순으로 나열하는 경우 탐색
        flag = True
        perm = list(perm)
        for i in range(n): # 현재 키의 사람이 주어진 array 값에 맞는 위치인지 판단
            count = 0
            for j in range(i):
                if perm[j] > perm[i]:
                    count += 1
            if array[perm[i] - 1] != count: # 아님
                flag = False
                break
            
        if flag: # 제대로 줄을 선 경우 출력
            for p in perm:
                print(p, end=' ')
            return

n = int(input())
array = list(map(int, input().split()))
solution(n, array)
'''