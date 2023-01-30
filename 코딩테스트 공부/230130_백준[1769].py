x = input()
cnt = 0

# 구현,수학,문자열/3의 배수/실버5

def three(num, cnt):
    if len(num) > 1:
        cnt += 1
        tmp = 0
        for i in num:
            tmp += int(i)
        three(str(tmp), cnt)
    else:
        if int(num) % 3 == 0:
            print(cnt)
            print("YES")
        else:
            print(cnt)
            print("NO")

three(x, cnt)
