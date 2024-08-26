import sys

input = sys.stdin.readline

def solution():
    n, score, p = map(int, input().split())
    count = 0
    if n == 0:  # 0
        return 1
    else:
        array = list(map(int, input().split()))
        if n == p:
            if array[-1] >= score:
                return -1
            for a in array:
                if score < a:
                    count += 1
            return count + 1
        else:
            for a in array:
                if score < a:
                    count += 1
            return count + 1

print(solution())