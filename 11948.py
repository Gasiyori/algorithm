a = []

for _ in range(6):
    a.append(int(input()))

b = a[0:4]
b.sort()
b.pop(0)

c = a[4:6]
c.sort()
c.pop(0)

print(sum(b) + sum(c))

# 0:4 중에서 3개 선택, 4:6중에 하나 선택