f = open("input.txt", "r")
n= int(f.readline())
temp = []
for _ in range(n):
    temp.append(list(map(int, f.readline().split())))

print(temp)

'''
아직 안품
'''
