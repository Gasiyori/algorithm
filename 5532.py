# 방학 일수 L, 풀어야 하는 개수 A, B, 하루 가능량 C, D

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

# 놀 수 있는 최대 날?
# 풀어야 하는 문제에서 하루 가능량을 빼다가 0 이하가 된 시점

count = 1 # 문제를 풀어야 하는 날짜

while (A - C) > 0 or (B - D) > 0:
    A = A - C
    B = B - D
    count = count + 1

print(L - count)