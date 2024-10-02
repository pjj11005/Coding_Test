def solution(people, limit):
    answer = 0
    people.sort()
    n = len(people)
    left, right = 0, n - 1
    
    while left <= right:
        total = people[left] + people[right]
        if total <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    return answer