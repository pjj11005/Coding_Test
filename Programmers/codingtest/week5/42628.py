import heapq

def solution(operations):
    maxheap = []
    minheap = []
    for operation in operations:
        op, num = operation.split()
        if op == 'I':  # 삽입
            heapq.heappush(minheap, int(num))
            heapq.heappush(maxheap, -int(num))
        else:  # 삭제
            if minheap:  # 데이터 있음
                if num == '-1':  # 최소
                    number = heapq.heappop(minheap)
                    maxheap.remove(-number)
                else:  # 최대
                    number = heapq.heappop(maxheap)
                    minheap.remove(-number)
    if not minheap:  # 비어있을 때
        return [0, 0]
    else:
        return [-maxheap[0], minheap[0]]