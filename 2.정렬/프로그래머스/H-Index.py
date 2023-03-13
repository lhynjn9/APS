def solution(citations):
    N = len(citations)
    citations.sort(reverse=True)

    for i in range(N):
        if citations[i] <= i:
            return i

    return N