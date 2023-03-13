from itertools import permutations


def solution(k, dungeons):
    answer = -1
    N = len(dungeons)
    lst = list(range(N))

    # 전체 경우의 수 탐색
    for i in range(N, 0, -1):
        for cases in permutations(lst, i):
            z = k
            check = True
            for j in cases:
                if z < dungeons[j][0]:
                    check = False
                    break
                else:
                    z -= dungeons[j][1]

            if check:
                return i

    return answer