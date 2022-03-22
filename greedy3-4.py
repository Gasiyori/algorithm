import sys

m, n = map(sys.stdin.readline().rstrip().split())

for i in range(m):
    data = list(map(int, input().split()))

    #이중 반복문 활용.
    #최소값을 먼저 찾아야 하므로 초기화는 문제 조건 최대값보다 큰 값을 줌
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
        
    result = max(result, min_value)

print(result)