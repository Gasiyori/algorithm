a = int(input()) # 원래 고기 온도
b = int(input()) # 목표 온도
c = int(input()) # 얼어있는 고기 1도 올리는데 걸리는 시간
d = int(input()) # 얼어있는 고기 해동 시간 
e = int(input()) # 얼어있지 않은 고기 1도 데우는데 걸리는 시간

if (0 < a):
    print(e * (b - a))
else: # 고기가 얼어 있을 때
    print((abs(a) * c) + d + (e * b))