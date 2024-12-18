import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_countries(o, p, q):
    p = find_parent(p)
    q = find_parent(q)

    if p == q:  # 이미 같은 집합인 경우
        return

    if o == 1:  # 동맹의 경우
        if p < q:
            power[p] += power[q]
            parent[q] = p
        else:
            power[q] += power[p]
            parent[p] = q
    else:  # 전쟁의 경우
        if power[p] > power[q]:
            power[p] -= power[q]
            power[q] = 0  # 패배한 나라의 병력은 0이 됨
            parent[q] = p
        elif power[p] < power[q]:
            power[q] -= power[p]
            power[p] = 0  # 패배한 나라의 병력은 0이 됨
            parent[p] = q
        else:  # 병력이 같은 경우 - 두 나라 모두 멸망
            power[p] = 0
            power[q] = 0
            parent[p] = 0
            parent[q] = 0

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
power = [0] + [int(input()) for _ in range(n)]

for _ in range(m):
    o, p, q = map(int, input().split())
    union_countries(o, p, q)

# 남아있는 국가 확인
countries = set()
result = []
for i in range(1, n+1):
    p = find_parent(i)
    if p != 0 and power[p] > 0:  # 멸망하지 않은 국가만 추가
        countries.add(p)

for c in countries:
    result.append(power[c])

result.sort()
print(len(result))
print(*result)