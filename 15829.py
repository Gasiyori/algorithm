from sys import stdin, stdout

l = int(stdin.readline().rstrip())

# a = ord('a') - 96
# abcde의 해시 값은 1 × 310 + 2 × 311 + 3 × 312 + 4 × 313 + 5 × 314 = 1 + 62 + 2883 + 119164 + 4617605 = 4739715이다.

a = stdin.readline().rstrip()

result = 0

for x in a:
    result += (ord(x) - 96) * (31 ** a.index(x))

stdout.write(str(result))