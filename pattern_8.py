# Ques) Print the given pattern.
# for n=5          for n=4
# 55555            4444
# 4444             333
# 333              22
# 22               1
# 1                    
# Solution-

n=int(input("Enter n:"))
for i in range (n):
	for j in range ((n-i),0,-1):
		print ((n-i),end="")
	print ()