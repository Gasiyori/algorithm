from sys import stdin, stdout

line = stdin.readline().rstrip()

while(line != ""):
    stdout.write(line + "\n")
    line = stdin.readline().rstrip()