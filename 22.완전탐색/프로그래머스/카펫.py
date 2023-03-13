def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            x = i  # 세로
            y = int(yellow // i)  # 가로

            # 그 경우의 수에 따른 갈색 구하기
            z = ((x + 2) * 2) + (y * 2)

            # 갈색 영역이 맞는지 비교
            if brown == z:
                answer.append(y + 2)
                answer.append(x + 2)
                break

    return answer