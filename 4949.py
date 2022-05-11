from sys import stdin, stdout

while True:
    ps = stdin.readline().rstrip()
    a = []
    top = 0

    if ps == ".":
        break
    
    for x in ps:
        if x == '(' or x == '[':
            a.append(x)
            top += 1

        elif x == ')':
            try:
                if a.pop() == '(':  
                    top -= 1
            except:
                top = -1
                break

        elif x == ']':
            try:
                if a.pop() == '[':
                    top -= 1
            except:
                top = -1
                break

    if top == 0:
        stdout.write("yes\n")
    else:
        stdout.write("no\n")