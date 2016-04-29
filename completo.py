x = input("Enter a number: ")
def completo (n):
	i = 2
	while n>1 and n>i:
		while n%i != 0:
			i = i+1
		n = n/i
		print i

completo(x)
