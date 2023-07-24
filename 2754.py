from sys import stdin, stdout

grade = stdin.readline().rstrip()

if grade == "A+":
    stdout.write("4.3")
elif grade == "A0":
    stdout.write("4.0")
elif grade == "A-":
    stdout.write("3.7")
elif grade == "B+":
    stdout.write("3.3")
elif grade == "B0":
    stdout.write("3.0")
elif grade == "B-":
    stdout.write("2.7")
elif grade == "C+":
    stdout.write("2.3")
elif grade == "C0":
    stdout.write("2.0")
elif grade == "C-":
    stdout.write("1.7")
elif grade == "D+":
    stdout.write("1.3")
elif grade == "D0":
    stdout.write("1.0")
elif grade == "D-":
    stdout.write("0.7")
else:
    stdout.write("0.0")