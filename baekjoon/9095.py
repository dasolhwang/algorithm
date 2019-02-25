'''
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
1+ 1+1+1
1+ 1+2
1+ 2+1
1+ 3

2+ 1+1
2+ 2

3+ 1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

7
44
274
'''

f = open("input.txt", "r")
n = int(f.readline())

def DP(k): # Top_down
    if k == 0:
        return 1
    elif k <= 2:
        return k
    else:
        return DP(k - 1) + DP(k - 2) + DP(k - 3)

for _ in range(n):
    k = int(f.readline())
    print(DP(k))