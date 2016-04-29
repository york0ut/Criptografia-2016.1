x = input("Enter a number: ")
def ingenuo (n):
	i = 2
	while n > 1:
		z = n
		n = n/i
		if n % i != 0:
			i = i + 1
	print z	

ingenuo(x)
