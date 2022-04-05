from math import sqrt


l = int(input())
# 삼각형 4개 중 2개씩 모양이 같음.
# 그 중 하나는 정삼각형 2개 넓이, 하나는 정삼각형 1개 넓이이므로 정삼각형 1개만 구함

print((sqrt(3) / 4) * (l ** 2))