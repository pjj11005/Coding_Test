import sys
input = sys.stdin.readline

def solution(s):
    s = s.upper()
    count = {}
    for i in s:
        if i not in count.keys():
            count[i] = 1
        else:
            count[i] += 1
    sorted_count = sorted(count.items(), key=lambda item:-item[1])
    if len(sorted_count) > 1: # 문자 여러개
        if sorted_count[0][1] == sorted_count[1][1]: # 여러개
            return '?'
        else:
            return sorted_count[0][0]
    else:
        return sorted_count[0][0]
    
print(solution(input().strip()))