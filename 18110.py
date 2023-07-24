from sys import stdin, stdout

n = int(stdin.readline().rstrip())
users = [0] * n

if n == 0:
    stdout.write("0")
else:
    users = []

    for x in range(n):
        users.append(int(stdin.readline().rstrip()))

    trim_mean = int((n*0.15)+0.5)

    users.sort()

    if trim_mean != 0:
        users = users[trim_mean:-trim_mean]

    stdout.write(str(int((sum(users)/len(users))+0.5)))