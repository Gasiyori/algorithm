from sys import stdin

a, b = map(int, stdin.readline().rstrip().split())
c = int(input())

# 시작 시간, 필요 시간 주어지면 끝나는 시간 계산
# a = 시, b = 분

# a가 24가 되면 0으로 변환
# b가 60이 되면 0으로 변환 + a에 + 1 or 2
# 한번에 시간이 2개씩 넘어갈수도 있으므로 캐리 사용

carry = (b + c) // 60 #정수값만 받도록 함

if (carry): #캐리가 있으면 구문 실행
    a = a + carry

b = (b + c) % 60 # 60으로 나눈 나머지 값(분)

# if a >= 24:
#     a = a - 24 # 이런식으로 풀긴 했는데

a = a % 24 # 생각해보니까 이게 더 나은듯

print(f"{a} {b}")