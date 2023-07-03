# CCW알고리즘,기하학/CCW/골드5

point1 = list(map(int,(input().split())))
point2 = list(map(int,(input().split())))
point3 = list(map(int,(input().split())))

a = point1[0]*point2[1]+point2[0]*point3[1]+point3[0]*point1[1]
b = point1[1]*point2[0]+point2[1]*point3[0]+point3[1]*point1[0]

if a-b > 0:
  print(1)
elif a-b == 0:
  print(0)
else:
  print(-1)
