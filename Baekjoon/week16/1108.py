import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_scc(node, stack):
    global scc_counter, vertex_counter
    # 노드 발견 순서 기록
    vertex_counter += 1
    discover[node] = vertex_counter
    stack.append(node)
    # 해당 노드가 도달할 수 있는 가장 일찍 발견된 노드
    parent = discover[node]

    for next_node in graph[node]:
        if discover[next_node] == 0: # 미방문 노드인 경우
            parent = min(parent, find_scc(next_node, stack))
        elif not finished[next_node]: # 방문했지만 아직 SCC 처리가 안 된 노드
            parent = min(parent, discover[next_node])

    if parent == discover[node]: # SCC 발견
        current_scc = []
        while True:
            top = stack.pop()
            current_scc.append(top)
            finished[top] = True # 노드 처리 완료 표시
            scc_number[top] = scc_counter # SCC 번호 할당
            if top == node: # 현재 노드까지 도달하면 종료
                break
        scc_list.append(current_scc) # SCC 리스트에 추가
        scc_counter += 1 # SCC 카운터 증가
    return parent

n = int(input())
graph = defaultdict(list)
websites = set()
# 웹사이트 정보 저장
for _ in range(n):
    info = input().split()
    target = info[0]
    count = int(info[1])
    websites.add(target)
    for i in range(count):
        source = info[i + 2]
        graph[source].append(target)
        websites.add(source)

# SCC 관련 변수 초기화
discover = defaultdict(int)
finished = defaultdict(bool)
scc_number = defaultdict(int)
scc_list = []
vertex_counter = 0
scc_counter = 0

# SCC 찾기
for website in websites:
    if not discover[website]:
        find_scc(website, [])

# SCC 그래프 생성
scc_graph = [set() for _ in range(scc_counter)] # 각 scc 그룹에서 다른 scc로 가는 링크 저장
indegree = [0] * scc_counter # scc 그룹의 진입 차수

for node in graph:
    for next_node in graph[node]:
        scc1, scc2 = scc_number[node], scc_number[next_node]
        if scc1 != scc2 and next_node not in scc_graph[scc1]:
            scc_graph[scc1].add(next_node)
            indegree[scc2] += 1

# 점수 계산
score = defaultdict(lambda : 1)
q = deque()

for i in range(scc_counter):
    if indegree[i] == 0:
        q.append(i)

while q:
    curr_scc = q.popleft()

    for next_node in scc_graph[curr_scc]:
        next_scc = scc_number[next_node]
        indegree[next_scc] -= 1

        for node in scc_list[curr_scc]:
            if next_node in graph[node]:
                score[next_node] += score[node]
                
        if indegree[next_scc] == 0:
            q.append(next_scc)
            
print(score[input().strip()])