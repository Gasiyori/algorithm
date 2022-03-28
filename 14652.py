# 세로 길이 N, 가로 길이 M, N <= M

# N x M 배열

from sys import stdin

n, m, k = map(int, stdin.readline().rstrip().split())

# # 리스트 컴프리헨션으로 2차원 배열 초기화.
# # 0으로 이루어진 배열을 m개 만들고, 이를 n번 반복
# array = [[0] * m for _ in range(n)] 

print(f"{(k // m)} {(k % m)}")