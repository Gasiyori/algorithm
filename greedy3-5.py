from sys import stdin, stdout

# 1이 될 때까지
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.

n, k = map(int, stdin.readline().rstrip().split())

count = 0

while True:
    if n == 1: # loop 탈출 조건
        break

    if (n % k) != 0 : # n이 k의 배수가 아닌 경우
        n = n - 1
    else : # 나누어서 1이 될 수 있는 경우
        n = n // k
        
    count += 1

stdout.write(str(count))

"""
# 교재 해결법

n, k = map(input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k # n을 k로 나누어서 누적하는 연산
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

"""