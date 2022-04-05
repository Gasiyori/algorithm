a, b = map(int, input().split())
c, d = map(int, input().split())

# a와 c가 사과, b와 d가 오렌지
# 1  2   ,   3  4
# 1  3 ,  3  4

# 사과랑 오렌지 각각에서 어느 쪽을 옮기는게 더 효율적인지 먼저 구해야 함.
# a와 c의 차, b와 d의 차를 구해서 더 큰 쪽(사과, 오렌지) 중 작은 단위를 먼저 옮겨야 함

count = 0

if (abs(a - c) > abs(b - d)): # 사과 옮기는게 더 효율적인 경우
    if a < c: #c가 더 많다면
        count = a + d # a를 오른쪽으로 옮기고 오렌지를 왼쪽으로 옮기는 경우의 수 더함
    else: # a가 더 많다면
        count = c + b # c를 왼쪽으로 옮기고 오렌지를 오른쪽으로 옮기는 경우의 수 더함
else: # 오렌지를 옮기는게 더 효율적인 경우
    if b < d: #d가 더 많다면
        count = b + c
    else:
        count = d + a

print(count)