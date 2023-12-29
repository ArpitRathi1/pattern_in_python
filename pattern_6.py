# Ques) Print the given pattern.
# for n=3        for n=4
# ***            ****
# **             ***
# *              **
#                *
# Solution-

n=int(input("Enter n:"))
for i in range (n):
	for j in range (n-i):
		print("*",end="")
	print()