s, t, d = map(int, input().split())

# 기차 속도 S, 파리 속도 T, 두 기차 사이 거리 D
# ex) 50, 75, 200

print(d // (s * 2) * t)