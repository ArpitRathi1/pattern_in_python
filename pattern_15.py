# Ques) Print the given pattern.
# for n=4          for n=5
# 1                1
# 21               21
# 321              321
# 4321             4321
#                  54321
# Solution-

n=int(input("Enter n:"))
for i in range (1,(n+1)):
	for j in range (i,0,-1):
		print(j,end="")
	print()