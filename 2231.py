from sys import stdin, stdout

n = int(stdin.readline().rstrip())

num = 0 # 1부터 계속 증가하는 숫자
sum = 0 # 분해합

for x in range(n):
    sum = num # 숫자의 분해합 구하기
    for y in str(num):
        sum += int(y)

    if sum == n:
        break

    num += 1

if sum == n:
    stdout.write(str(num))
else:
    stdout.write('0')