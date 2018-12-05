import sys

r = lambda: sys.stdin.readline().strip()
n = int(r())

def function(n):
	for i in range(n):
		command = r()
		cnt=0
		for j in range(len(command)):
			if command[j]=="(":
				cnt+=1
			else:
				cnt-=1
			if cnt < 0:
				return "NO"

		if cnt==0:
			return "YES"
		else: return "NO"


def function_stack(n):
	for i in range(n):
		command = r()
		stack=[]
		for j in range(len(command)):
			if command[j]=="(":
				stack.append(command[j])
			else:
				if len(stack)==0:
					return "NO"
				else:
					stack.pop()
		if len(stack)==0:
			return "YES"
		else : return "NO"

for i in range(n):
	print(function_stack(n))
