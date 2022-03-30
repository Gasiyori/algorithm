a, b, c = map(int, input().split())

if a == b and b == c: # 세 개가 모두 같은 경우
    print(10000 + (a * 1000))
elif a == b or b == c or c == a: # 2개가 같은 경우
    if a == b or a == c: # a값 기준
        print(1000 + (a * 100))
    else: # 그 외) b와 c가 같은 경우
        print(1000 + (b * 100))
elif a != b and b != c and c != a: # 세 개가 모두 다른 경우
    print(max(a, b, c) * 100)