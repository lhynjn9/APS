import sys
sys.stdin = open('input.txt')

P = int(input())
for i in range(P):
    res = 0
    student = list(map(int, input().split()))

    tc = student.pop(0)
    x = [] # 새로운 학생 줄
    x.append(student.pop(0)) # 첫번째 학생

    for i in student:
        if max(x) < i:
            x.append(i)

        else:
            for j in range(len(x)):
                if i < x[j]:
                    res += (len(x) - j)
                    x.insert(j, i)
                    break

    print(tc, res)