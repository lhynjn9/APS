import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    
    # str1의 딕셔너리 만들기
    str1_dict = {}

    for i in str1:
        str1_dict[i] = str1_dict.get(i, 0)

    for j in str2:
        if str1_dict.get(j) != None:
            str1_dict[j] = str1_dict.get(j, 0) + 1

    print(f'#{tc} {max(str1_dict.values())}')

