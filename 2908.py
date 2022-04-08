# 두 문자를 받아서
# 뒤집고
# 비교해서 큰 수 출력

a, b = input().split()

r_a, r_b = [], []

for x in a:
    r_a.append(x)

for x in b:
    r_b.append(x)

r_a.reverse()
r_b.reverse()

r_a = int("".join(r_a))
r_b = int("".join(r_b))

if r_a < r_b:
    print(r_b)
else:
    print(r_a)
