
# ( () [ [] ] )( [] )   => 28
'''
( [] )

'''

f = open("input.txt","r")
temp = f.readline()

stack = []
result = 0
cnt = 1
for i in range(len(temp)):
    if temp[i] == "(":
        stack.append("(")
    if temp[i] == ")":
        if stack[-1] == "(":
            stack.pop()
            stack.append(2)
        else:
            j=0
            while stack[len(stack)-j-2] != "(":
                if stack[len(stack)-j-2] not in ["[","]","(",")"]:
                    result +=

        else:
            stack.append(")")
    if temp[i] == "[":
        stack.append("[")
    if temp[i] == "]":
        if stack[-1] == "[":
            stack.pop()
            stack.append(3)

            stack.append("]")
print(stack)