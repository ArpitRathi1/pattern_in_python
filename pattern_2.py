# Ques) Print the given pattern.
# for n=3        for n=4
# 123            1234
# 123            1234
# 123            1234
#                1234
# Solution-

n=int(input("Enter n:"))

for i in range(1,(n+1)):
	for j in range(1,(n+1)):
		print(j,end="")
	print()