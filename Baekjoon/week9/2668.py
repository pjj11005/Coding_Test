import sys
input = sys.stdin.readline

def dfs(a, b): # 시작, 현재 좌표
    visited[b] = 1
    w = array[b]
    if not visited[w]:
        dfs(a, w)
    elif visited[w] and w == a:
        answer.append(w)
            
n = int(input())
array = [0] + [int(input()) for _ in range(n)]
answer = []

# 각 좌표를 돌며 사이클 판별
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    dfs(i, i)
    
answer.sort()
print(len(answer))
for a in answer:
    print(a)