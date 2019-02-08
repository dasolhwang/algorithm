f = open("input.txt","r")
T = int(f.readline())

for _ in range(T):
    ans = "#" + f.readline().strip()
    temp = list(map(int, f.readline().split()))
    length = []
    for i in set(temp):
        length.append([temp.count(i),i])

    print(ans,str(max(length)[1]))
