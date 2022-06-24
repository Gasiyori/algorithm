from sys import stdin, stdout

n = int(stdin.readline().rstrip())

count = 0

for h in range(n + 1): # n시 59분 59초까지이므로
    for m in range(60):
        for s in range(60):
            time = str(h) + str(m) + str(s)
            if '3' in time:
                count += 1

print(count)