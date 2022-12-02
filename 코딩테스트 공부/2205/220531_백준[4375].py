# 수학,브루트포스_1/실버3

while 1:
    try:
        n=int(input())
    except:
        break
    tmp=1
    cnt=1
    while tmp%n!=0:
        tmp=(tmp*10)+1
        cnt+=1
    print(cnt)