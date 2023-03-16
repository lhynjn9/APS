import sys
sys.stdin = open('input.txt')

while True:
    word = input()
    vowel = 'aeiou'

    if word == 'end':
        break

    vflag = 0 # 모음 존재 여부 확인
    vcnt = 0 # 모음 3개 확인
    ccnt = 0 # 자음 3개 확인
    err = 0 # 문자 연속 확인

    for i in range(len(word)):
        # 같은 문자 두번 연속
        if i > 0:
            if (word[i] == word[i-1]) and (word[i] != 'e' and word[i] != 'o'):
                err = 1
                break
        if word[i] in vowel:
            vflag = 1
            vcnt += 1
            ccnt = 0
            # 모음 연속 3개 확인
            if vcnt == 3:
                err = 1
                break
        else:
            vcnt = 0
            ccnt += 1
            if ccnt == 3:
                err = 1
                break
                
    if (err != 1) and (vflag == 1):
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')