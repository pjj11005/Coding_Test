def solution(phone_book):
    phone_dict = {}
    for phone in phone_book:
        phone_dict[phone] = 1

    for phone in phone_book:
        for i in range(1, len(phone)):
            prefix = phone[:i]
            if prefix in phone_dict.keys():
                return False
    return True

'''
풀이 : 모든 번호를 딕셔너리로 저장 -> 각 번호들의 접두어가 딕셔너리에 존재하는지 확인
다른 풀이 : 각 번호들의 가능한 접두어들 저장 -> 각 번호들의 접두어가 가능한지 확인
'''