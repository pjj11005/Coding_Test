import sys
input = sys.stdin.readline

def solution(n, game):
    name = set()
    for i in range(n):
        name.add(input())
    if game == 'Y': # 윷놀이
        return len(name)
    elif game == 'F': # 같은 그림 찾기
        return len(name) // 2
    else: # 원카드
        return len(name) // 3

n, game = input().split()
n = int(n)
print(solution(n, game))