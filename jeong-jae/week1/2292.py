import sys
input = sys.stdin.readline

def solution(n):
    answer = 1
    if n == 1:
        return answer
    else:
        num = 1
        while True:
            num += (answer * 6)
            if n <= num:
                return answer + 1
            answer += 1
print(solution(int(input())))