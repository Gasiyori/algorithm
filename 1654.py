from sys import stdin, stdout

# 랜선 개수 k, 필요한 길이 n
k, n = list(map(int, stdin.readline().rstrip().split()))

array = []

for _ in range(k):
    array.append(int(stdin.readline().rstrip()))

# 시작점, 끝점 설정
start = 1
end = max(array)

# 이진 탐색

while(start <= end):
    cnt = 0
    mid = (start + end) // 2

    # 잘랐을 때 랜선 길이 계산
    for x in array:
        cnt += x // mid

    # 부족하면 더 많이 자르기 (왼쪽 탐색)
    if cnt < n:
        end = mid - 1

    # 많으면 덜 자르기 (오른쪽 탐색)
    else:
        start = mid + 1

stdout.write(str(end))