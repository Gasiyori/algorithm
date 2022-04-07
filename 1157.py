n = input()

count = []
dict = {}
count.append(n.count('a') + n.count('A'))
count.append(n.count('b') + n.count('B'))
count.append(n.count('c') + n.count('C'))
count.append(n.count('d') + n.count('D'))
count.append(n.count('e') + n.count('E'))
count.append(n.count('f') + n.count('F'))
count.append(n.count('g') + n.count('G'))
count.append(n.count('h') + n.count('H'))
count.append(n.count('i') + n.count('I'))
count.append(n.count('j') + n.count('J'))
count.append(n.count('k') + n.count('K'))
count.append(n.count('l') + n.count('L'))
count.append(n.count('m') + n.count('M'))
count.append(n.count('n') + n.count('N'))
count.append(n.count('o') + n.count('O'))
count.append(n.count('p') + n.count('P'))
count.append(n.count('q') + n.count('Q'))
count.append(n.count('r') + n.count('R'))
count.append(n.count('s') + n.count('S'))
count.append(n.count('t') + n.count('T'))
count.append(n.count('u') + n.count('U'))
count.append(n.count('v') + n.count('V'))
count.append(n.count('w') + n.count('W'))
count.append(n.count('x') + n.count('X'))
count.append(n.count('y') + n.count('Y'))
count.append(n.count('z') + n.count('Z'))

dict[0] = 'A'
dict[1] = 'B'
dict[2] = 'C'
dict[3] = 'D'
dict[4] = 'E'
dict[5] = 'F'
dict[6] = 'G'
dict[7] = 'H'
dict[8] = 'I'
dict[9] = 'J'
dict[10] = 'K'
dict[11] = 'L'
dict[12] = 'M'
dict[13] = 'N'
dict[14] = 'O'
dict[15] = 'P'
dict[16] = 'Q'
dict[17] = 'R'
dict[18] = 'S'
dict[19] = 'T'
dict[20] = 'U'
dict[21] = 'V'
dict[22] = 'W'
dict[23] = 'X'
dict[24] = 'Y'
dict[25] = 'Z'

m = count.index(max(count))

count.sort(reverse=True)

if (count[0] == count[1]):
    print("?")
else:
    print(dict[m])