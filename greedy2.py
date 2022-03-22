# 배열이 존재할 때, M번 더하여 가장 큰 수를 만드는 방법
# 단, 연속으로 K번을 초과하여 더해질 수 없음
# 배열의 크기 N, 숫자가 더해지는 횟수 M, K가 주어질 때 결과 출력
# 둘째 줄에 N개의 자연수

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

first = data[0]
second = data[1]

total = 0
repeat = 0

for __ in range(m): # m번 반복
    if repeat < k:
        total += first
        repeat = repeat + 1
    else:
        total += second
        repeat = 0

print(total)