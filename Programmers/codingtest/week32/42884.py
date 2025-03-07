def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[1])  # 진출 지점 기준 정렬
    camera = -30001  # 카메라 위치

    # 카메라 설치
    for x, y in routes:
        # 진입 지점 > 현재 카메라 위치 : 설치 필요
        if x > camera:
            answer += 1
            camera = y  # 카메라 진출 지점에 설치

    return answer
