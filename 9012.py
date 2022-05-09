from sys import stdin, stdout

n = int(stdin.readline().rstrip())

for _ in range(n):
    ps = stdin.readline().rstrip()
    a = []
    top = 0

    for x in ps:
        if x == '(':
            top += 1
            a.append(x)
        elif x == ')':
            top -= 1
            try:
                a.pop()
            except:
                break
        else:
            continue
    
    if top == 0:
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")