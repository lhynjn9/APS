import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]
    sols = []
    for i in range(15):  # 문자열의 길이(행)
        for j in range(5):  # 단어의 수(열)
            if i < len(arr[j]):  # 특정 문자열의 길이가 해당 문자열을 순회할때 보다 크면, 해당 글자는 없으므로 미출력
                sols.append(arr[j][i])  # i와 j의 순서 유의
    print(f'#{tc} {"".join(sols)}')