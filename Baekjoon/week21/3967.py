import sys

input = sys.stdin.readline


# 합 체크 함수
def check(idx, star_list, groups):
    for group in groups:
        if group[-1] >= idx:  # 아직 끝나지 않은 줄 pass
            continue
        if sum(star_list[i] for i in group) != 26:  # 합이 26 아님
            return False
    return True


# 결과 출력 함수
def print_result(star_list, index_list, array):
    for i, (x, y) in enumerate(index_list):
        if array[x][y] == "x":  # 빈칸 채우기
            array[x][y] = chr(star_list[i] + ord("A") - 1)
    for row in array:
        print("".join(row))


# dfs 탐색 함수
def dfs(idx, array, index_list, groups, star_list, visited):
    # 각 줄이 완성 될 때
    if idx in [5, 8, 11, 12]:
        if not check(idx, star_list, groups):  # 불가능
            return False
        if idx == 12:  # 종료
            print_result(star_list, index_list, array)
            return True

    if star_list[idx] > 0:  # 이미 존재
        return dfs(idx + 1, array, index_list, groups, star_list, visited)

    # 새로운 값 채우기
    for i in range(1, 13):
        if not visited[i]:
            star_list[idx] = i
            visited[i] = 1
            if dfs(idx + 1, array, index_list, groups, star_list, visited):
                return True
            star_list[idx] = 0
            visited[i] = 0
    return False


# 숫자로 변환하는 함수
def encode(array, index_list, star_list, visited):
    for i in range(12):
        x, y = index_list[i]
        if array[x][y] != "x":
            star_list[i] = ord(array[x][y]) - ord("A") + 1
            visited[star_list[i]] = 1


def main():
    array = [list(input().strip()) for _ in range(5)]

    # 각 위치 저장
    index_list = [(0, 4), (1, 1), (1, 3), (1, 5), (1, 7), (2, 2), (2, 6), (3, 1), (3, 3), (3, 5), (3, 7), (4, 4)]
    # 각 줄의 인덱스
    groups = [(0, 2, 5, 7), (0, 3, 6, 10), (7, 8, 9, 10), (1, 2, 3, 4), (1, 5, 8, 11), (4, 6, 9, 11)]

    star_list = [0] * 12  # 숫자 저장 리스트
    visited = [0] * 13  # 사용된 알파벳(숫자) 체크

    encode(array, index_list, star_list, visited)
    dfs(0, array, index_list, groups, star_list, visited)


if __name__ == "__main__":
    main()
