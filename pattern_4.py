# Ques) Print the given pattern.
# for n=3       for n=4
# 1             1
# 12            12
# 123           124
#               1234
# Solution-

n=int(input("Enter n:"))
for i in range(1,(n+1)):
	for j in range(1,(i+1)):
		print(j,end="")
	print()
