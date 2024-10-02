def solution(arr):
    answer = []
    num = arr[0]
    answer.append(num)
    for i in range(1, len(arr)):
        if num != arr[i]:  # 다를 때
            num = arr[i]
            answer.append(num)

    return answer
