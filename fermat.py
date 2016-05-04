import math
from math import sqrt

def fermat(n):
	x =  math.ceil(sqrt(n))
	y = sqrt (x*x-n)
	aux = int(sqrt(x*x-n)) - sqrt(x*x-n)
	while aux != 0:
		x = x+1
		y = sqrt (x*x-n)
		aux = int(sqrt(x*x-n)) - sqrt(x*x-n)
	p = x+y
	q = x-y
	print p
	print q

fermat(101)
