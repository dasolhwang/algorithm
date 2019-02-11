'''
비트연산 ---> 시간초과
'''

f = open("input.txt", "r")
n = int(f.readline())
S = 0

for i in range(n):
    temp = f.readline().split()
    if temp[0] == "add":
        S |= (1 << int(temp[1]))
    if temp[0] == "remove":
        S &= ~(1 << int(temp[1]))
    if temp[0] == "check":
        if S & (1 << int(temp[1])):
            print(1)
        else:
            print(0)
    if temp[0] == "toggle":
        if S & (1 << int(temp[1])):
            S &= ~(1 << int(temp[1]))
        else:
            S |= (1 << int(temp[1]))
    if temp[0] == "all":
        S = (1 << 21) - 1
    if temp[0] == "empty":
        S = 0




