from sys import stdin, stdout

n = stdin.readline().rstrip()

x = ['1', '2', '3', '4', '5', '6', '7', '8'] # 행
y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # 열

# 현재 좌표 만들기(1~8 기준으로)
nx = x.index(n[1]) + 1
ny = y.index(n[0]) + 1

count = 0

if ny - 2 >= 1 and nx - 1 >= 1:
    count += 1

if ny - 2 >= 1 and nx + 1 <= 8:
    count += 1

if ny + 2 <= 8 and nx + 1 <= 8:
    count += 1

if ny + 2 <= 8 and nx - 1 >= 1:
    count += 1

if ny - 1 >= 1 and nx - 2 >= 1:
    count += 1

if ny - 1 >= 1 and nx + 2 <= 8:
    count += 1

if ny + 1 <= 8 and nx - 2 >= 1:
    count += 1

if ny + 1 <= 8 and nx + 2 <= 8:
    count += 1

print(count)

# """
input_data = input()
row = int(input_data[1]) # 행
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 열

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0] # 현재 위치에서 steps의 각 요소(step) 중 0번째 항목(x위치)로 다음 위치 확인
    next_column = column + step[1] # 위와 동일. 1번째 항목(y위치)로 다음 위치 확인
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
# """