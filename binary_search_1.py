# 재귀함수로 구현

def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2 # 중간 값

    # 찾으면 중간점 인덱스 반환
    if array[mid] ==  target:
        return mid

    # 타겟보다 중간점이 더 크면 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    
    # 타겟보다 중간점이 더 작으면 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)