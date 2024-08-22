import sys
input = sys.stdin.readline

def solution(s):
    minimum = int(1e9)
    a = s.count('a')
    s += s[:a - 1] # 원형이라 배열 2개 합치기
    for i in range(len(s) - (a - 1)):
        minimum = min(minimum, s[i:i + a].count('b'))
    return minimum

s = list(input().strip())
print(solution(s))

'''
a의 총 갯수 크기의 슬라이스 윈도우를 만들고 인덱스를 증가시키면서 해당 부분을 모두 a로 바꾸는 횟수를 리스트에 저장
'''