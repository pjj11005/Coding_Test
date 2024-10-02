def solution(sizes):
    maximum, minimum = max(sizes[0]), min(sizes[0])
    for i in range(1, len(sizes)):
        maximum = max(maximum, max(sizes[i]))
        minimum = max(minimum, min(sizes[i]))
    return maximum * minimum