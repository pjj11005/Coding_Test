import sys
input = sys.stdin.readline

def solution(n, m, l, k, array):
    # 별똥별 좌표를 x 기준으로 정렬
    stars = sorted(array)
    answer = 0

    # 모든 별똥별의 x 좌표에 대해 탐색
    for i in range(k):
        x1 = stars[i][0]
        x2 = x1 + l

        # 현재 x 범위에 포함된 y 좌표들을 수집하고 정렬
        y_coords = [y for x, y in stars if x1 <= x <= x2]
        y_coords.sort()

        # 슬라이딩 윈도우로 y 범위 안의 최대 별똥별 개수 찾기
        left = 0
        for right in range(len(y_coords)):
            while y_coords[right] - y_coords[left] > l: # 범위의 크기가 L보다 크면 왼쪽 포인터 앞으로 
                left += 1
            answer = max(answer, right - left + 1)

    return k - answer

n, m, l, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(k)]
print(solution(n, m, l, k, array))
