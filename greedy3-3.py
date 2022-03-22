import sys

# m, n을 입력받음
# m은 행 개수, n은 열 개수
m, n = map(int, sys.stdin.readline().rstrip().split())

result = 0

# 행 개수만큼 반복
for i in range(m):
    data = list(map(int, sys.stdin.readline().rstrip().split()))

    # 현재 값 중 가장 작은 수 탐색
    min_value = min(data)

    # 가장 작은 수 중에 가장 큰 수 탐색
    result = max(result, min_value)


# 매 루프마다 result에 max로 넣는 방법도 있지만 append로 배열을 만들어서 가장 큰 값만 max로 뽑아와도 될 듯
print(result)