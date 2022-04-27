from sys import stdin, stdout

n = int(stdin.readline().rstrip())

count = n % 8

if count == 1:
    stdout.write("1")
elif count == 2 or count == 0:
    stdout.write("2")
elif count == 3 or count == 7:
    stdout.write("3")
elif count == 4 or count == 6:
    stdout.write("4")
else:
    stdout.write("5")