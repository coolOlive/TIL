from collections import deque

# 시간초과 주의하자!

def solution(queue1, queue2):
    q1, q2=deque(queue1), deque(queue2)
    sum1=sum(q1)
    mid=(sum1+sum(q2))//2
    
    if max(q1)>mid or max(q2)>mid or int(mid)!=mid:
        return -1
    
    cnt=0
    while q1 and q2:
        if sum1==mid:
            return cnt
        elif sum1>mid:
            sum1-=q1.popleft()
        else:
            q1.append(q2.popleft())
            sum1+=q1[-1]
        cnt+=1
    
    return -1