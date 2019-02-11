'''
L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $	$라는 문자를 커서 왼쪽에 추가함
'''

f = open("input.txt", "r")
temp = f.readline().strip()
n = int(f.readline().strip())

rstack = []
lstack = [i for i in temp]
for i in range(n):
    k = f.readline().strip()
    if k[0] == "L":
        if len(lstack) != 0:
            rstack.append(lstack[-1])
            lstack.pop()
    if k[0] == "D":
        if len(rstack) != 0:
            lstack.append(rstack[-1])
            rstack.pop()
    if k[0] == "B":
        if len(lstack) != 0:
            lstack.pop()
    if k[0] == "P":
        lstack.append(k[2])

while len(lstack) != 0:
    rstack.append(lstack[-1])
    lstack.pop()

result = ""
while len(rstack) != 0:
    result += rstack[-1]
    rstack.pop()

print(result)