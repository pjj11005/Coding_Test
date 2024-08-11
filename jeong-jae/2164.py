import sys
input = sys.stdin.readline

def solution(n):
    if n == 1:
        return 1
    else:
        num = 1
        while num < n:
            num *= 2
        if num == n: # 2의 제곱수
            return num
        else: # 2의 제곱수 아님
            return num - (2 * (num - n))
        
n = int(input())
print(solution(n))