from sys import stdin, stdout

t = int(stdin.readline().rstrip())

# k는 층, n은 호

for _ in range(t):
    k = int(stdin.readline().rstrip())
    n = int(stdin.readline().rstrip())

    array = [[0] * (n + 1) for _ in range(k + 1)]

    for y in range(k + 1):
        for x in range(n):
            if x == 0: # 층 수 관계없이 1호는 무조건 1명
                array[y][x] = 1
                # print(y, x, array[y][x])
            elif y == 0: # 0층인 경우 1, 2, 3 순서대로,,,
                array[y][x] = x + 1 
                # print(y, x, array[y][x])
            else: # 그 외의 층인 경우?
                array[y][x] = array[y - 1][x] + array[y][x - 1]
                # print(y, x, array[y][x])
                
    stdout.write(str(array[k][n - 1]) + '\n')