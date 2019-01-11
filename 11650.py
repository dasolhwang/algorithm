'''
1 -1
1 1
2 2
3 3
3 4
'''

f = open("input.txt", "r")

ans = []
for _ in range(int(f.readline())):
    m, n = map(int, f.readline().split())
    ans.append((m,n))

for i in sorted(ans):
    print(i[0], i[1])
