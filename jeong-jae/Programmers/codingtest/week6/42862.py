def solution(n, lost, reserve):
    answer = 0
    array = [1] * n
    for l in lost:
        array[l - 1] = 0
    
    for r in sorted(reserve): # 정렬하여 앞에서부터 빌려주도록
        if r in lost:
            array[r - 1] = 1
            continue
        
        for x in (-1, 1):
            if 0 <= r + x - 1 < n and array[r + x - 1] == 0:
                array[r + x - 1] = 1
                break
        
    answer = array.count(1)
    return answer