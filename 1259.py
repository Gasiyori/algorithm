from sys import stdin, stdout

while(1):
    a = stdin.readline().rstrip()
    b = "".join(reversed(a))

    if a == '0':
        break
    elif a == b:
        stdout.write("yes\n")
    else:
        stdout.write("no\n")