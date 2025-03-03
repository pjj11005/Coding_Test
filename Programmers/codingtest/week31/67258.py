def solution(gems):
    n = len(set(gems))  # 보석의 총 종류 수
    gem_dict = {}  # 현재 구간에 포함된 보석들을 저장할 딕셔너리
    answer = [1, len(gems)]  # 초기 답안 설정 (전체 구간)
    start, end = 0, 0  # 투 포인터 초기화

    while end < len(gems):
        gem_dict[gems[end]] = gem_dict.get(gems[end], 0) + 1
        end += 1

        # 현재 구간에 모든 종류의 보석이 포함되면
        while len(gem_dict) == n:
            # 더 짧은 구간 찾으며 업데이트
            if end - start < answer[1] - answer[0] + 1:
                answer = [start + 1, end]

            # start 이동
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]]
            start += 1

    return answer
