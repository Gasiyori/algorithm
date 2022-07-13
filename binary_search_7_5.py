from sys import stdin, stdout

# 부품 개수/번호
n = int(stdin.readline().rstrip())
array1 = list(map(int, stdin.readline().rstrip().split()))

# 찾고자 하는 부품 개수/번호
m = int(stdin.readline().rstrip())
array2 = list(map(int, stdin.readline().rstrip().split()))

def binary_search(array, target, start, end):
    while(start <= end):
        mid = (start + end) // 2

        if target == array[mid]:
            stdout.write("yes ")
            return mid

        elif target < array[mid]:
            end = mid - 1

        else:
            start = mid + 1

    stdout.write("no ")
    return None

array1.sort()

for x in array2:
    binary_search(array1, x, 0, n - 1)