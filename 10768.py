m = int(input())
d = int(input())

if m < 2: # 2월 이전이면
    print("Before")

elif m == 2: #2월인 경우
    if d < 18: #18일 이전
        print("Before")
    elif d == 18:
        print("Special")
    else:
        print("After")

else: #2월 이후인 경우
    print("After")