from functools import cmp_to_key

def compare(a, b):
    # a+b와 b+a를 비교하여 더 큰 순으로 정렬
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0


def solution(numbers):
    # 숫자 문자열 리스트를 비교 함수에 따라 정렬
    numbers = [str(num) for num in numbers]
    sorted_numbers = sorted(numbers, key=cmp_to_key(compare))

    largest_number = ''.join(sorted_numbers)

    # 만약 가장 큰 수가 "0"으로 시작하면, 전체가 "0"이라는 의미
    if largest_number[0] == '0':
        return '0'

    return largest_number