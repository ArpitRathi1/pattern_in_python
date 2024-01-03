# Ques) Print the given pattern.
# for n=4         for n=5
# 1               1
# 22              22
# 333             333
# 4444            4444
#                 55555
# Solution-

n=int(input("Enter n:"))
for i in range (1,(n+1)):
	for j in range (i):
		print(i,end="")
	print()