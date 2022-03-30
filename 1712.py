from sys import stdin

# 고정비용 a, 가변비용b, 가격c
# 손익분기점 넘기기
# a + (count)b > (count)c

a, b, c = map(int, stdin.readline().rstrip().split())

# 손익분기점이 존재하지 않는 경우 => 가변비용이 가격과 같거나 비싼 경우, 즉 b >= c

# 수식으로 맞춰끼우자면...
# c에서 b를 뺀 값으로 a를 나누고 +1
# 가격에서 가변비용을 뺀 값을 고정비용으로 나누면 손익분기점이 나옴
# 그 이상부터 수익이 나기 때문에 1을 더해줌

if b >= c: 
    print(-1)
else:
    print((a // (c - b)) + 1)

