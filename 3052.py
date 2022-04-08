a = []

for _ in range(10):
    a.append(int(input()))

for x in range(10):
    a[x] = a[x] % 42

print(len(set(a)))