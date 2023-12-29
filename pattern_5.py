# # Ques) Print the given pattern.
# for n=3      for n=4
# A            A
# AB           AB
# ABC          ABC
#              ABCD
# Solution-

n=int(input("Enter n:"))
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range (1,n+1):
	for j in range(i):
		print(alpha[j],end="")
	print()