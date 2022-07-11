# 문자열,정렬_도비의 난독증 테스트/실버5
# 12시가 지나버려서 깃헙 잔디 빠져버림..

while True:
    n=int(input())
    if n==0:
        break
    words=[]
    for _ in range(n):
        w=input().strip()
        words.append(w)
    words.sort(key=lambda x:x.upper())
    print(words[0])