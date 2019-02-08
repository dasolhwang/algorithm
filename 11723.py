'''
비트연산 ---> 시간초과
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다.
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.
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




