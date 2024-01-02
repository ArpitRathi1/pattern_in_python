# Ques) print the given pattern.
# for n=3         for n=4
# A               A
# BC              BC
# DEF             DEF
#                 GHIJ
# Solution-

n=int(input("Enter n:"))
alpha="ABCDEFGHIJLMNOPQRSTUVWXYZ"
a=0
for i in range (1,(n+1)):
	for j in range (i):
		print(alpha[a],end="")
		a=a+1
	print()