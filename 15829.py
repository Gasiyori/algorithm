from sys import stdin, stdout

l = int(stdin.readline().rstrip())

# a = ord('a') - 96
# abcde의 해시 값은 1 × 31^0 + 2 × 31^1 + 3 × 31^2 + 4 × 31^3 + 5 × 31^4 = 1 + 62 + 2883 + 119164 + 4617605 = 4739715이다.

a = stdin.readline().rstrip()

result = 0

for x in range(l):
    result += (ord(a[x]) - 96) * (31 ** x)

result = result % 1234567891

stdout.write(str(result))