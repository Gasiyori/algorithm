from sys import stdin, stdout

# 떡의 개수 n, 요청한 떡의 길이 m
n, m = list(map(int, stdin.readline().rstrip().split()))

# 각 떡의 개별 높이 정보
array = list(map(int, stdin.readline().rstrip().split()))

# 시작점, 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행

result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2

    # 잘랐을 때 떡의 양 계산
    for x in array:
        if x > mid:
            total += x - mid
        
    # 떡의 양이 부족하면 더 많이 자르기 (왼쪽 탐색)
    if total < m:
        end = mid - 1

    # 떡의 양이 많으면 덜 자르기 (오른쪽 탐색)
    else:
        result = mid
        start = mid + 1

stdout.write(str(result))