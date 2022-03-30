# 인치, 높이와 너비 비율일 때 실제 높이 너비 길이 출력

from math import sqrt

d, h, w = map(int, input().split())

# 높이 비율 / 너비 비율 = 실제 높이 / 실제 너비

# 피타고라스 정리에 의해 가로:세로:대각선 비율의 공식은 다음과 같음
# a^2 + b^2 = c^2

# 해당 공식을 이용하여 가로:세로:대각선의 비율을 구했으므로 실제 값에 의한 계산을 해야 함.
# 너비 비율이 w, 높이 비율이 h이고 실제값 d로 대각선의 비율 c를 구하면

rate = d / sqrt(h**2 + w**2) # d / c로, 대각선의 1비율당 길이를 알 수 있음

height = int(rate * h)
width = int(rate * w)

print(f"{height} {width}")