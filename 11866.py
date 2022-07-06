from sys import stdin, stdout
from collections import deque

# n은 배열 길이, k는 반복 간격
n, k = map(int, stdin.readline().rstrip().split())

# 1부터 n까지의 배열 생성
array = deque([i for i in range(1, n + 1)])

array2 = []

while len(array) != 0:            
    array.rotate(-(k - 1))
    
    array2.append(array.popleft())

stdout.write("<" + str(array2)[1:-1] + ">")