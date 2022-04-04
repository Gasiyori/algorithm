a = []

for _ in range(3):
    a.append(int(input()))

if sum(a) == 180: # 삼각형일 때
    if a[0] == a[1] and a[1] == a[2]: # 세 각의 크기가 모두 60일 때
        print("Equilateral")
    elif a[0] == a[1] or a[1] == a[2] or a[2] == a[0]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
