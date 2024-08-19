import sys
input = sys.stdin.readline

def solution(array, x, y, z):
    rank = 1
    for a, b, c in array:
        if a == x: # 금메달 수 같음
            if b == y: # 은메달 수 같음
                if c > z: # 동메달 수 적음
                    rank += 1
            elif b > y: # 은메달 수 적음
                rank += 1
        elif a > x: # 금메달 더 적음
            rank += 1
    return rank

n, k = map(int, input().split())
x, y, z = 0, 0, 0
array = []
for i in range(n):
    num, a, b, c = map(int, input().split())
    if num == k:
        x, y, z = a, b, c
    array.append((a, b, c))
print(solution(array, x, y, z))
