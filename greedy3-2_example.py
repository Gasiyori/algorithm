#특정 수열 형태로 일정하게 반복되는 특징을 이용

n, m, k = map(int, input().split())

data = list(map(input().split()))

data.sort()

first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1) * k)
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)