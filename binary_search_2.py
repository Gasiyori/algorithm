# 반복문으로 구현

def binary_serach(array, target, start, end):
    while start <= end: # 하나의 값으로 만날때까지
        mid = (start + end) // 2

        if array[mid] ==  target: # 중간점을 찾으면 반환
            return mid
        elif array[mid] > target: # 타겟의 값이 중간점보다 작으면
            end = mid - 1 # 끝 값 줄이기
        else: # 타겟의 값이 중간점보다 크면
            start = mid + 1 # 시작 값 늘리기

    return None

n, target = list(map(int, input().split()))

array = list(map(int, input().splilt()))

result = binary_serach(array, target, 0, n - 1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)