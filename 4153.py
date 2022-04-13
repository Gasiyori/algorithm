from sys import stdin, stdout

while(1):
    a = []

    for x in (map(int, stdin.readline().rstrip().split())):
        a.append(x)

    a.sort()

    line1, line2, line3 = a

    if line1 == 0 and line2 == 0 and line3 == 0:
        break
    elif ((line1**2) + (line2**2)) == (line3**2):
        stdout.write('right\n')
    else:
        stdout.write('wrong\n')