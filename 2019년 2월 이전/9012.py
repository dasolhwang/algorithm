
def VPS(text):
    stack = []
    for i in text:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

for _ in range(int(input())):
    if VPS(input()) == True:
        print("YES")
    else:
        print("NO")
