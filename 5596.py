from sys import stdin

a = list(map(int, stdin.readline().rstrip().split())) #점수
b = list(map(int, stdin.readline().rstrip().split())) #점수

# a와 b 둘의 총 점수 중 더 큰 점수 출력

result1 = 0
result2 = 0

for i in range(len(a)):
    result1 = result1 + int(a[i])
    result2 = result2 + int(b[i])

print(max(result1, result2))