import sys
input = sys.stdin.readline

def is_possible(s): # 암호 가능 여부
    v = ['a', 'e', 'i', 'o', 'u']
    v_count, c_count = 0, 0 # 모음, 자음 카운트
    for x in s:
        if x in v:
            v_count += 1
        else:
            c_count += 1
    if v_count >= 1 and c_count >= 2:
        return True
    return False

def dfs(index, s):
    if len(s) == l:
        if is_possible(s):
            print(s)
        return
    
    for j in range(index + 1, c):
        dfs(j, s + array[j])

l, c = map(int, input().split())
array = list(input().strip().split())
array.sort()
for i in range(c - l + 1):
    dfs(i, array[i])