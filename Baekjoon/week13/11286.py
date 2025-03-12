import sys
import heapq

input = sys.stdin.readline


def solution():
    n = int(input())
    q = []
    for _ in range(n):
        x = int(input())

        # 출력
        if x == 0:
            if not q:
                print(0)
            else:
                _, b = heapq.heappop(q)
                print(b)
        # 삽입
        else:
            heapq.heappush(q, (abs(x), x))  # 절대값, 원래값


def solution2():
    n = int(input())
    posH = []  # 양수
    negH = []  # 음수

    for i in range(n):
        x = int(input())

        if x == 0:
            # 둘다 비어있음
            if len(posH) == 0 and len(negH) == 0:
                print(0)
            # 양수 비어있음
            elif len(posH) == 0:
                print(-heapq.heappop(negH))
            # 음수 비어있음
            elif len(negH) == 0:
                print(heapq.heappop(posH))
            else:
                # 절대값 비교, 같은 경우에도 음수 쪽에서 뺌(실제값 고려)
                if posH[0] >= negH[0]:
                    print(-heapq.heappop(negH))
                else:
                    print(heapq.heappop(posH))
        else:
            if x > 0:
                heapq.heappush(posH, x)
            else:
                heapq.heappush(negH, -x)

    return


if __name__ == "__main__":
    solution()
