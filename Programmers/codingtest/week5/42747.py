def solution(citations):
    citations.sort(reverse=True)
    answer = citations[0]
    while True:
        count = 0
        for cite in citations:
            if cite >= answer:
                count += 1

        if count >= answer:
            break
        answer -= 1

    return answer