def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:  # 참가 안함
            answer = participant[i]
            break
    if not answer:  # 참가자 마지막 사람이 참가 안함
        answer = participant[-1]

    return answer
