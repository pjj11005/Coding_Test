def solution(word):
    answer = 0
    array = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    for i in range(1, 6):
        if i == 1:
            for a in array:
                dictionary.append(a)
        elif i == 2:
            for a in array:
                for b in array:
                    dictionary.append(a + b)
        elif i == 3:
            for a in array:
                for b in array:
                    for c in array:
                        dictionary.append(a + b + c)
        elif i == 4:
            for a in array:
                for b in array:
                    for c in array:
                        for d in array:
                            dictionary.append(a + b + c + d)
        else:
            for a in array:
                for b in array:
                    for c in array:
                        for d in array:
                            for e in array:
                                dictionary.append(a + b + c + d + e)
    
    dictionary.sort()
    answer = dictionary.index(word) + 1
    return answer