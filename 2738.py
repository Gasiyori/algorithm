from sys import stdin, stdout

n, m = map(int, stdin.readline().rstrip().split())

arrA = []
arrB = []

for _ in range(n):
    arrA.append(list(map(int, stdin.readline().rstrip().split())))

for _ in range(n):
    arrB.append(list(map(int, stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(m):
        stdout.write(str(arrA[i][j] + arrB[i][j]) + " ")
    stdout.write("\n")