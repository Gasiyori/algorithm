from sys import stdin, stdout

# n개의 원소, k번의 바꿔치기, 배열 A와 B

# k번 이내의 바꿔치기 연산을 통해 만들 수 있는 배열 A의 모든ㅇ ㅝㄴ소 합이 최대가 되도록

n, k = map(int, stdin.readline().rstrip().split())

array_a = list(map(int, stdin.readline().rstrip().split()))
array_b = list(map(int, stdin.readline().rstrip().split()))

array_a.sort() # 오름차순 정렬 (1 2 3 4 5)
array_b.sort(reverse=True) # 내림차순 정렬 (5 4 3 2 1)

count = 0 # 바꿔치기 최대 수만큼 세기

while(count < k and array_a[count] < array_b[count]):
    if array_a[count] < array_b[count]:
        array_a[count], array_b[count] = array_b[count], array_a[count] # 값 swap
        count += 1

# for문 사용시
"""
for i in range(k):
    if array_a[i] < array_b[i]:
        array_a[count], array_b[count] = array_b[count], array_a[count] # 값 swap
    else:
        break
"""
stdout.write(str(sum(array_a)))