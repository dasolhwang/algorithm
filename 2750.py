import sys

n = int(input())
x = []
for i in range(n):
    x.append(int(input()))
# BubbleSort
for i in range(n):
    for j in range(n - 1):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]
for i in x:
    print(i)
    
# SelectionSort
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if x[min_idx] > x[j]:
            min_idx = j
    if min_idx != i:
        x[i], x[min_idx] = x[min_idx], x[i]
    print(x[i])

# InsertionSort
for i in range(1, n):
    for j in range(i-1, -1, -1):
        if x[i] < x[j]:
            x[i], x[j] = x[j], x[i]
            i = j
        else:
            break
for i in x:
    print(i)
