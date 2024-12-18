import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000  # cm를 나노미터로 변환
        n = int(input())
        lego = [int(input()) for _ in range(n)]
        lego.sort()  # 이분 탐색을 위한 정렬
        
        left, right = 0, n-1
        found = False
        
        while left < right:
            total = lego[left] + lego[right]
            if total == x:
                print(f'yes {lego[left]} {lego[right]}')
                found = True
                break
            elif total < x:
                left += 1
            else:
                right -= 1
                
        if not found:
            print('danger')
            
    except:
        break