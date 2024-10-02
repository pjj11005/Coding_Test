def solution(answers):
    answer = []
    n = len(answers)
    maximum = 0
    solution_a = [1, 2, 3, 4, 5]
    solution_b = [2, 1, 2, 3, 2, 4, 2, 5]
    solution_c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    array = []  # (번호, 맞춘 수)
    for idx, solution in enumerate([solution_a, solution_b, solution_c]):
        s = len(solution)
        count = 0
        if n % s == 0:  # 배수
            full_solution = solution * (n // s)
        else:  # 나누어 떨어지지 않을 때
            full_solution = solution * (n // s)
            full_solution += solution[:n % s]

        for i in range(n):  # 채점
            if answers[i] == full_solution[i]:
                count += 1
        maximum = max(maximum, count)  # 최댓값 갱신
        array.append((idx + 1, count))

    for idx, count in array:
        if maximum == count:
            answer.append(idx)
    return answer
