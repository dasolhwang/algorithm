'''
2×n 직사각형을 1x2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
171
'''

f = open("input.txt","r")
n = int(f.readline())

def bottom_up(n):
    D = [0]*(n+1)
    for i in range(n+1):
        if i <= 1:
            D[i] = 1
        else:
            D[i] = D[i-1] + 2*D[i-2]
    return D[n]
print(bottom_up(n)%10007)


def top_down(n):
    if n <= 2:
        return n
    else:
        return (top_down(n-1) + 2*top_down(n-2))

print(top_down(n)%10007)
