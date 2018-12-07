import sys
queue = []
for _ in range(int(sys.stdin.readline())):
    temp = sys.stdin.readline().split()
    if temp[0] == "push":
        queue.append(int(temp[1]))
    if temp[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    if temp[0] == "size":
        print(len(queue))
    if temp[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if temp[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    if temp[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
