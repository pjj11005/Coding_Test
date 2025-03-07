import sys

input = sys.stdin.readline


# 먹이 정보 추가
def add_food(tree, foods):
    curr = tree
    for food in foods:
        # 현재 위치에 해당 먹이 없으면
        if food not in curr:
            # 새로운 딕셔너리 생성
            curr[food] = {}
        # 다음 단계로 이동
        curr = curr[food]


# 먹이 정보 재귀적으로 출력
def print_food(tree, depth=0):
    for food in sorted(tree.keys()):
        print("--" * depth + food)
        print_food(tree[food], depth + 1)


def solution():
    n = int(input())
    tree = {}

    # 먹이 정보 담기
    for _ in range(n):
        info = list(input().strip().split())
        add_food(tree, info[1:])

    print_food(tree)


if __name__ == "__main__":
    solution()
