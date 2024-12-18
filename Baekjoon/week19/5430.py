import sys
from collections import deque
input = sys.stdin.readline

def solution(p, array):
    is_reverse = 0 # 뒤집힘 유무
    # 연산 수행
    for cmd in p:
        if cmd == 'R': # reverse
            is_reverse = 1 - is_reverse
        else: # delete
            if not array: # empty
                return 'error'
                
            if not is_reverse: # original
                array.popleft()
            else: # reverse
                array.pop()

    if is_reverse: # reverse
        array.reverse()
    return '[' + ','.join(array) + ']'
    
for _ in range(int(input())):
    p = input().strip()
    n = int(input())
    array = list(input().strip()[1:-1].split(','))
    
    if n == 0: # empty
        array = deque()
    else:
        array = deque(array)

    print(solution(p, array))