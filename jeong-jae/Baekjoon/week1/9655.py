import sys
input = sys.stdin.readline

def solution(n):
    if n % 2 == 0:
        print('CY')
    else:
        print('SK')
solution(int(input()))