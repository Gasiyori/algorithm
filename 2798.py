from sys import stdin, stdout

n, m = map(int, stdin.readline().rstrip().split())

# 3장을 골라 m을 넘지 않는 선에서 최대한 가깝게.

card = list(map(int, stdin.readline().rstrip().split()))

result = 0

for i in range(0, n - 2): # 0부터 시작, 3개를 골라야 하므로 뒤에서 3번째까지만 반복
    for j in range(i + 1, n - 1): # 1부터 시작, 뒤에서 2번째까지만 반복
        for k in range(j + 1, n): # 2부터 시작, 끝까지 반복
            # 세 카드의 합이 m보다 같거나 작고, result보다 큰 경우
            if (card[i] + card[j] + card[k]) <= m and (card[i] + card[j] + card[k]) > result:
                result = card[i] + card[j] + card[k]

stdout.write(str(result))