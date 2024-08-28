import sys
input = sys.stdin.readline

def solution(s):
    zero, one = 0, 0
    for i in s:
        if i == '0':
            zero += 1
        else:
            one += 1
    zero //= 2
    one //= 2
    
    if one > 0:
        for i in s: # 1 제거
            s.remove('1')
            one -= 1
            if one == 0:
                break
    
    s.reverse()
    if zero > 0:
        for i in s: # 0 제거
            s.remove('0')
            zero -= 1
            if zero == 0:
                break
    
    s.reverse()
    return ''.join(s)

s = list(input().strip())
print(solution(s))