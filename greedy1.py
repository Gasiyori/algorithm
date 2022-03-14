# 거스름돈을 줄 때, 최소한의 동전 개수는?

n = 1260 # 입력값(거스름돈)
count = 0

# 동전 개수
coin_types = [500, 100, 50, 10]

for coin in coin_types: # 큰 단위 동전부터 하나씩 확인하여 누적함
    count += n // coin # 입력값(거스름돈)을 큰 단위 동전부터 나누어서 개수 저장
    n %= coin # 나머지 값만큼 누적하여 저장

print(count)