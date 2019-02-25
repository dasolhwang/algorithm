# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# a b c d e f g h i j k l m n o p q r s t u v w x y z

f = open("input.txt","r")
word = f.readline()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = [0 for i in range(len(alphabet))]
for i in word:
    for idx, j in enumerate(alphabet):
        if i == j:
            result[idx] += 1
temp = ""
for i in result:
    temp = temp +"{} ".format(i)
print(temp)