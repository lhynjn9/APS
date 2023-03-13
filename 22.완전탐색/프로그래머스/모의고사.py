def solution(answers):
    answer = []

    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    x = len(a)
    y = len(b)
    z = len(c)

    q = len(answers)

    a = a * (q // x + 1)
    b = b * (q // y + 1)
    c = c * (q // z + 1)

    w = [0] * 3

    for i in range(len(a)):
        if i == q:
            break
        else:
            if a[i] == answers[i]:
                w[0] += 1
            if b[i] == answers[i]:
                w[1] += 1
            if c[i] == answers[i]:
                w[2] += 1

    s = max(w)

    for j in range(len(w)):
        if s == w[j]:
            answer.append(j + 1)

    return answer