# Ques) Print the given pattern.
# for n=3         for n=4  
# 123             1234
# 12              123
# 1               12
#                 1
# Solution-

n=int(input("Enter n:"))
for i in range (n):
	for j in range (1,(n-i+1)):
		print(j,end="")
	print()