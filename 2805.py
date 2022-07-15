from sys import stdin, stdout

# 개수 n, 가져가려는 길이 m
n, m = map(int, stdin.readline().rstrip().split())
array = list(map(int, stdin.readline().rstrip().split()))
start, end = 1, max(array)

while start <= end:
    result = 0
    mid = (start + end) // 2

    for x in array:
        if x >= mid:
            result += x - mid
    
    if result < m: # 남은 길이의 합이 가져가려는 길이보다 적으면 더 많이 자르기
        end = mid - 1

    else:
        start = mid + 1

stdout.write(str(end))