import sys

input = sys.stdin.readline
INF = int(1e9)

def dfs(idx, plus, minus, multi, div, total, n, array):
    global maximum, minimum  # 전역 변수로 선언

    if idx == n - 1:  # 종료 조건
        maximum = max(maximum, total)
        minimum = min(minimum, total)
        return
    
    if plus:  # 더하기
        dfs(idx + 1, plus - 1, minus, multi, div, total + array[idx + 1], n,  array)
    
    if minus:  # 빼기
        dfs(idx + 1, plus, minus - 1, multi, div, total - array[idx + 1], n, array)
    
    if multi:  # 곱하기
        dfs(idx + 1, plus, minus, multi - 1, div, total * array[idx + 1], n, array)
    
    if div:  # 나누기
        dfs(idx + 1, plus, minus, multi, div - 1, int(total / array[idx + 1]), n, array)

def main():
    global maximum, minimum  # 전역 변수로 선언

    n = int(input())
    array = list(map(int, input().split()))
    plus, minus, multi, div = map(int, input().split())  # 연산자 개수 입력

    # 초기 최대/최소값 설정
    maximum, minimum = -INF, INF

    # DFS 함수 호출
    dfs(0, plus, minus, multi, div, array[0], n, array)

    print(maximum)
    print(minimum)

if __name__ == '__main__':
    main()
