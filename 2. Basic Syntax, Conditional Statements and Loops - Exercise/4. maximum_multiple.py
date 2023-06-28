import sys

divisor = int(input())
boundary = int(input())

max_num = - sys.maxsize

for i in range(0, boundary+1):
    if i % divisor == 0:
        max_num = i

print(max_num)
