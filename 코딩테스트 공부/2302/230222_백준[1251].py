# 브루트포스,정렬,문자열/단어 나누기/실버5

word = list(input())
ans = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word) ):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        ans.append(''.join(a + b + c))

print(min(ans))
