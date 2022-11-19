import sys
input=sys.stdin.readline

# 스택/후위 표기식2/실버3

n = int(input())
operator = input().strip()
nums = [int(input()) for _ in range(n)]
    
stack = []

for i in operator :					
    if 'A' <= i <= 'Z':
        stack.append(nums[ord(i) - ord('A')])
    else :
        tmp1 = stack.pop()
        tmp2 = stack.pop()
        
        if i =='+' :
            stack.append(tmp1+tmp2)
        elif i == '-' :
            stack.append(tmp2-tmp1)
        elif i == '*' :
            stack.append(tmp1*tmp2)
        elif i == '/' :
            stack.append(tmp2/tmp1)

print('%.2f'%stack[0])