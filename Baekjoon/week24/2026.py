import sys
from collections import defaultdict

input = sys.stdin.readline


# x가 나머지 모두랑 친구인지 체크
def check(friends, selected, new_friend):
    for s in selected:
        if new_friend not in friends[s]:
            return False
    return True


# dfs로 친구 관계 찾기
def dfs(k, n, friends, selected, current):
    # 친구 관계 출력
    if len(selected) == k:
        for num in selected:
            print(num)
        exit(0)

    # 친구 찾기
    for i in range(current, n + 1):
        # 친구 k 이상 가능해 보이면
        if len(friends[i]) >= k - 1:
            if check(friends, selected, i):
                dfs(k, n, friends, selected + [i], i + 1)


def solution():
    k, n, f = map(int, input().split())
    friends = defaultdict(set)
    for _ in range(f):
        a, b = map(int, input().split())
        friends[a].add(b)
        friends[b].add(a)

    # 친구 관계 출력
    dfs(k, n, friends, [], 1)
    print(-1)  # 없으면 -1


if __name__ == "__main__":
    solution()
