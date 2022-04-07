n = int(input())

for _ in range(n):
    r, s = input().split()
    r = int(r)
    for i in s:
        print(i * r, end='')
    print()
