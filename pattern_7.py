# Ques) print the given pattern.
# for n=4
#    1
#   123
#  12345
# 1234567

# Solution-

n=int(input("Enter n:"))
for i in range (1,(n+1)):
	print(" " * (n-i),end="")
	for j in range (1,(2*i-1+1)):
		print(j,end="")
	print()
