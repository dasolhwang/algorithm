f = open("input.txt", "r")
n = int(f.readline())

'''
(1) (1 ~ n-1) 원탑을 x에서 z로 옮기기
(2) n 원탑을 x에서 y로 옮기기
(3) (1 ~ n-1) 원탑을 z에서 y로 옮기기
'''
temp = []
def solve(n,x,y):
    if n == 0:
        return
    solve(n-1, x, 6-x-y) # (1)
    temp.append([x,y])
    solve(n-1, 6-x-y, y) # (3)

solve(n,1,3)

print(len(temp))
for tmp in temp:
    print(tmp[0], tmp[1])