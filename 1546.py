n = int(input())

a = list(map(int, input().split()))

b = []

for x in range(n):
    b.append((a[x]/max(a)) * 100)

print(sum(b) / len(b))