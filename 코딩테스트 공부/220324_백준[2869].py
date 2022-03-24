a,b,v=map(int,input().split())
loca=(v-a)/(a-b)+1
print(int(loca)) if loca==int(loca) else print(int(loca)+1)

"""
틀린 풀이 => 반복문으로 풀면 시간초과 뜬다! 수학적 계산으로 풀어야 했다.
a,b,v=map(int,input().split())
loca=0
day=0

while loca<v:
    loca+=a
    day+=1
    if loca>=v:
        break
    loca-=b

print(day)
"""