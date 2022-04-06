# 스택_균형잡힌 세상/실버4

while True:
    s = input()
    if s == '.':
        break
    stack = []
    is_yes=True

    for a in s:
        if a=='(' or a=='[':
            stack.append(a)
        elif a==')':
            if len(stack)==0 or stack[-1]=='[':
                is_yes=False
                break
            else:
                stack.pop()
        elif a==']':
            if len(stack)==0 or stack[-1]=='(':
                is_yes=False
                break
            else:
                stack.pop()
    if is_yes==True and len(stack)==0:
        print("yes")
    else:
        print("no")