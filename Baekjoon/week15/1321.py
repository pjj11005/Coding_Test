import sys
input = sys.stdin.readline

# 펜윅 트리 업데이트 함수
def update_fenwick(i, v):
    while i <= N:
        fenwick[i] += v
        i += i & -i

# 펜윅 트리에서 k번째 병사가 속한 그룹을 찾는 함수
def find_kth_soldier(k):
    idx = 0
    bit_mask = 1 << 19  # 최대 범위 설정 (2^19)
    
    while bit_mask:
        next_idx = idx + bit_mask
        if next_idx <= N and fenwick[next_idx] < k:
            k -= fenwick[next_idx]
            idx = next_idx
        bit_mask >>= 1
    
    return idx + 1

# 입력 처리
N = int(input())  # 그룹의 개수
data = list(map(int, input().split()))  # 각 그룹의 병사 수

# 펜윅 트리 초기화
fenwick = [0] * (N + 1)

# 초기 데이터로 펜윅 트리 구성
for i in range(1, N + 1):
    update_fenwick(i, data[i - 1])

# 쿼리 처리
Q = int(input())  # 쿼리의 개수

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:  # 병사 추가 쿼리
        group_idx = query[1]
        num_soldiers = query[2]
        update_fenwick(group_idx, num_soldiers)
    
    elif query[0] == 2:  # k번째 병사가 속한 그룹 찾기 쿼리
        k = query[1]
        print(find_kth_soldier(k))