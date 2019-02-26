'''
n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다.
이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때,
프리오더를 구하는 프로그램을 작성하시오.

인오더    : L root R   (가운데 인)
포스트오더 : L  R  root (마지막)
-------------------------------
프리오더  : root L  R   (앞)
'''

'''
import sys
sys.setrecursionlimit(10**6)
'''
f = open("input.txt", "r")
n = int(f.readline())
in_order = list(map(int, f.readline().split()))
post_order = list(map(int, f.readline().split()))

position = [0 for _ in range(n)]
for i in range(n):
    position[in_order[i]-1] = i

result = []
def solve(in_start, in_end, post_start, post_end):
    if (in_start > in_end)|(post_start > post_end):
        return

    root = post_order[post_end]
    result.append(root)
    pr = position[root-1]
    solve(in_start, pr-1, post_start, post_start+pr-in_start-1)
    solve(pr+1, in_end, post_start+pr-in_start, post_end-1)

solve(0,n-1,0,n-1)
print(str(result)[1:-1].replace(",",""))
