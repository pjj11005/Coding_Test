import sys

input = sys.stdin.readline


def solution():
    while True:
        s = input().strip()
        # 종료
        if s == "*":
            return

        flag = True
        # 간격 증가
        for i in range(1, len(s)):
            visited = set()
            # 단어 생성
            for j in range(len(s) - i):
                x = s[j] + s[j + i]
                if x not in visited:
                    visited.add(x)
                else:  # 유일 X
                    flag = False
                    break
            # 유일 X
            if not flag:
                break

        # surprising
        if flag:
            print(f"{s} is surprising.")
        # not surprising
        else:
            print(f"{s} is NOT surprising.")


if __name__ == "__main__":
    solution()
