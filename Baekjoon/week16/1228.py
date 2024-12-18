''' 풀이 실패패
from collections import defaultdict
import heapq

def calculate_min_conquest_time(N, M, country_data):
    conquest_time = {}
    subordinates = defaultdict(list)
    indegree = defaultdict(int)

    # 국가 데이터 읽기
    for data in country_data:
        parts = data.split()
        country = parts[0]
        time = int(parts[1])
        conquest_time[country] = time
        for sub in parts[2:]:
            subordinates[country].append(sub)
            indegree[sub] += 1

    # 우선순위 큐를 사용하여 정복 시간이 가장 짧은 국가 선택
    queue = []
    for country in conquest_time:
        if indegree[country] == 0:
            heapq.heappush(queue, (conquest_time[country], country))

    total_time = 0
    conquered = set()
    count = 0

    while queue and count < M:
        time, country = heapq.heappop(queue)

        if country in conquered:
            continue

        conquered.add(country)
        total_time = max(total_time, time)
        count += 1

        # 속국들 처리
        stack = [country]
        while stack:
            current = stack.pop()
            for sub in subordinates[current]:
                if sub not in conquered:
                    conquered.add(sub)
                    count += 1
                    stack.append(sub)
                    if count >= M:
                        return total_time

        # 새로운 정복 가능 국가 추가
        for country in conquest_time:
            if country not in conquered and indegree[country] == 0:
                heapq.heappush(queue, (conquest_time[country], country))

    return total_time

# 입력 처리
N, M = map(int, input().split())
country_data = [input() for _ in range(N)]

# 결과 계산 및 출력
min_conquest_time = calculate_min_conquest_time(N, M, country_data)
print(min_conquest_time)
'''