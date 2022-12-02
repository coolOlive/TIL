import math

def solution(n, k):
    answer = 0
    jinsu=''
        
    while n>0:
        jinsu=str(n%k)+jinsu
        n//=k
    
    sosu=jinsu.split('0')

    for a in sosu:
        if a!='1' and a!='':
            answer+=1
            for i in range(2,int(math.sqrt(int(a)))+1):
                if int(a)%i==0:
                    answer-=1
                    break
    
    return answer