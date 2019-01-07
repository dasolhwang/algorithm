import sys
r = lambda : sys.stdin.readline().strip()

# 쇠막대기
f = open("input.txt", "r")
temp = f.readline()

stack = []
cnt = 0

for idx, i in enumerate(temp):
    if i == "(":
        stack.append(idx)
    if i == ")":
        if idx - stack[-1] == 1:
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)



