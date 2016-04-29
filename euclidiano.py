x = input("Enter a number: ")
y = input("Enter a second number: ")

def mdcEstendido(a, b):
	r = a
	x1 = 1
	x2 = 0
	b1 = b
	a1 = a
	while r > 0:
		q = a / b
		xtemp = x1 - q*x2
		mdc = r
		r = a % b
		a = b
		b = r
		x1 = x2
		x2 = xtemp
	beta = (mdc - a1*x1)/b1
	alfa = x1
	print mdc, alfa, beta
	return mdc, alfa, beta
	
mdcEstendido(x, y)

