def solution(s):
    stack=[]
    
    for a in s:
        if len(stack)==0:
            stack.append(a)
        elif stack[-1]==a:
            stack.pop()
        else:
            stack.append(a)

    return 1 if len(stack)==0 else 0