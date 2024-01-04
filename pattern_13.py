# Ques) Print the given pattern.
# for n=4          for n=5
# 4444             55555
# 333              4444
# 22               333
# 1                22
#                  1
# Solution-

n=int(input("Enter n:"))
for i in range (n):
	for j in range ((n-i),0,-1):
		print((n-i),end="")
	print()