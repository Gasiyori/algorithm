from sys import stdin, stdout

n = int(stdin.readline().rstrip())

count = n // 5

"""
경우의 수 파악

1. 3으로 나누어지는 경우
2. 5로 나누어지는 경우
3. 3과 5로 나누어지는 경우
4. 나누어지지 않는 경우 (-1)


"""