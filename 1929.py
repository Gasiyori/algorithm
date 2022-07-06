from math import sqrt
from sys import stdin, stdout

m, n = map(int, stdin.readline().rstrip().split()) # M이랑 N

array = [True for i in range(n + 1)] # 0은 무시
array[1] = False # 1은 소수가 아님

for i in range(2, int(sqrt(n) + 1)): # n의 제곱근까지 확인하면서
    if array[i]: # array[i]가 True면
        j = 2
        while i * j <= n: # 해당 i를 제외한 i의 배수는 False로 변환
            array[i * j] = False
            j += 1

for i in range(m, n + 1):
    if array[i] == True:
        stdout.write(str(i) + '\n')