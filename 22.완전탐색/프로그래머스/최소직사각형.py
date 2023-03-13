def solution(sizes):
    x = 0
    y = 0

    for i in range(len(sizes)):
        a = max(sizes[i])
        b = min(sizes[i])

        if x < a:
            x = a
        if y < b:
            y = b

    answer = x * y

    return answer