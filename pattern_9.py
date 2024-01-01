# Print the given pattern.
# for n=3       for n=4
# 1             1
# 23            23
# 456           456
#               78910
# Solution-

n=int(input("Enter n:"))
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a=0
for i in range(1,(n+1)):
	for j in range(i):
		print(lst[a],end="")
		a=a+1
	print()