# Ques) Print the given pattern.
# for n=4         for n=5
# 1111            11111
# 222             2222
# 33              333
# 4               44
#                 5
# Solution-

n=int(input("Enter n:"))
for i in range(n):
	for j in range(n-i):
		print(i+1,end="")
	print()