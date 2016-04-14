def parteImpar (n):
	e = 0
	q = n
	while (q % 2 == 0):
		e = e+1
		q = q/2
	print q, e
parteImpar(1000)
