n = 8
k = [4,3,6,8,7,5,2,1]

stack = []
result = []
temp = 0
for i in k:
    if (len(stack) == 0) | (i > temp):
        for j in range(temp+1, i+1):
            stack.append(j)
            result.append("+")
        temp = j
        stack.pop()
        result.append("-")
    elif i == stack[-1]:
        stack.pop()
        result.append("-")

if len(stack) != 0:
    print("NO")
    print(stack)
else:
    for i in result:
        print(i)