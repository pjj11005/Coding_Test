import sys
input = sys.stdin.readline

def solution(n, array):
    for i in range(n):
        count = 1
        x, y = array[i]
        for j in range(n):
            if i != j: # 본인 아닐 때
                p, q = array[j]
                if x < p and y < q: # 나보다 큰 사람 만남
                    count += 1
        print(count, end=' ')
                
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
solution(n, array)