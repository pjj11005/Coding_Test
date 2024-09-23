import sys
input = sys.stdin.readline

def dfs(string, depth):
    if depth == n:
        ans = eval(string.replace(' ', ''))
        if ans == 0:
            answer.append(string)
        return
    
    # 붙이기
    dfs(string + ' ' + str(depth + 1), depth + 1)
    # 더하기
    dfs(string + '+' + str(depth + 1), depth + 1)
    # 빼기
    dfs(string + '-' + str(depth + 1), depth + 1)
    
for _ in range(int(input())):
    n = int(input())
    answer = []
    dfs('1', 1)
    for a in answer:
        print(a)
    print()
