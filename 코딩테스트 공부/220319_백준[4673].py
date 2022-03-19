#오늘부터 1일 1커밋 도전!
natural_list=set(range(1,10001))
not_self=set()


# 셀프넘버가 아닌 값을 not_self에 추가해주는 함수
def is_self(num):
    for a in str(num):
        num+=int(a)
    not_self.add(num)

#함수 호출
for i in natural_list:
    is_self(i)

self_num=sorted(natural_list-not_self)

for result in self_num:
    print(result)
