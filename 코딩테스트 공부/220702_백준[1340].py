import re

# 구현,문자열,파싱_연도 진행바/실버5 **

s=input().strip()
date=re.split(r'[ ,:]',s)
mon_list=['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']
days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if int(date[3])%400 == 0 or (int(date[3])%4 == 0 and int(date[3])%100 != 0):
    days[1] += 1

sum_time=sum(days)*24*60

month=mon_list.index(date[0])
now=(sum(days[:month])+int(date[1])-1)*24*60+int(date[4])*60+int(date[5])

print(now/sum_time*100)