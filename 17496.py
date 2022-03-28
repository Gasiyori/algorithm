# i+T에 수확
# 수확한 날에도 심기 가능

# 빈 칸 c개 있음

# N일까지 여름, N일 지나면 버려짐

# 판매하면 P원 범

# 여름 일 수 N, 자라는데 걸리는 일 수 T, 칸 수 C, 개당 가격 P

from sys import stdin

n, t, c, p = map(int, stdin.readline().rstrip().split())

# 나머지는 버려야하므로 //연산
# 첫째날도 계산에 넣어야 됨
result = ((n-1) // t) * c * p

print(result)