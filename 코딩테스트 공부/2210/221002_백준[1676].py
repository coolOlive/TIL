 # 수학,큰수계산/팩토리얼 0의 개수/실버5

n=int(input())
cnt=0

while n!=0:
    n//=5
    cnt+=n

print(cnt)