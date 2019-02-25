f = open("input.txt", "r")
word = f.readline()

result = []
for i in range(len(word)):
    result.append(word[i:])

result = sorted(result)
for i in result:
    print(i)