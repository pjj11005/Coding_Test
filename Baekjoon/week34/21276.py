import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    names = list(input().split())
    child, level = {name: [] for name in names}, dict.fromkeys(names, 0)
    m = int(input())

    # 정보 저장
    for _ in range(m):
        a, b = input().split()
        level[a] += 1  # 레벨 증가
        child[b].append(a)

    # 루트 출력
    roots = sorted([key for key, item in level.items() if item == 0])
    print(len(roots))
    print(*roots)

    # 자식 출력
    for key, item in sorted(child.items()):
        if item:
            item = sorted(item, key=lambda x: (level[x], x))  # (레벨, 사전)순 정렬
            min_level = level[item[0]]  # 가장 낮은 레벨
            new_item = []
            # 바로 아래 자식만 담음
            for i in item:
                if level[i] == min_level:
                    new_item.append(i)
            child[key] = new_item
            print(key, len(new_item), *new_item)
        else:
            print(key, len(item))


if __name__ == "__main__":
    solution()
