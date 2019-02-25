f = open("input.txt", "r")

ans = []
for _ in range(int(f.readline())):
    m, n = map(int, f.readline().split())
    ans.append((n,m))

for i in sorted(ans):
    print(i[1], i[0])
