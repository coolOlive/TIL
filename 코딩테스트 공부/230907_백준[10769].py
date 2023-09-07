# 문자열,파싱/행복한지 슬픈지/브론즈1

icon = input()
smile = icon.count(":-)")
sad = icon.count(":-(")

if smile==0 and sad==0:
  print("none")
elif smile==sad:
  print("unsure")
elif smile>sad:
  print("happy")
elif smile<sad:
  print("sad")

