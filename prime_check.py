from math import sqrt
from sys import stdin, stdout

n = int(stdin.readline().rstrip())

array = [True for i in range(n + 1)] # 0은 무시

for i in range(2, int(sqrt(n) + 1)): # n의 제곱근까지 확인하면서
    if array[i]: # array[i]가 True면
        j = 2
        while i * j <= n: # 해당 i를 제외한 i의 배수는 False로 변환
            array[i * j] = False
            j += 1

count = 0

for i in range(1, len(array)):
    if array[i] == True:
        count += 1

stdout.write(str(count))