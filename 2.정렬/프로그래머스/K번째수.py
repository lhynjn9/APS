def solution(array, commands):
    answer = []
    
    for i in commands:
        a = i[0] - 1
        b = i[1]
        c = i[2]-1
        lst = array[a:b]
        
        lst.sort()
        
        x = lst[c]
    
        answer.append(x)
        
    return answer