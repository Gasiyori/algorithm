import sys

read1 = sys.stdin.readline().rstrip()
print(read1)
#입력받기
#문자열도 가능
#readline()이 input()보다 빠름

read2 = list(map(int, input().split()))
print(read2)
#입력 받아서 인트형으로 변환하는 함수를 매핑

read3 = list(map(int, sys.stdin.readline().rstrip().split()))
print(read3)
#이런식으로 하면 좀 더 빠르긴 할 듯?