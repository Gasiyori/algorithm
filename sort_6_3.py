array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 0번째 index는 자체로 정렬되어 있다고 판단 (즉, 1번째 index부터 삽입 실행)
    for j in range(i, 0, -1): # i부터 0까지 순회
        if array[j] < array[j - 1]: # 현재 index의 값을 왼쪽의 index와 비교해서 값이 작으면
            array[j], array[j - 1] = array[j - 1], array[j] # swap
        else:
            break

print(array)