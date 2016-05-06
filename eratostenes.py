def CrivoDeEratostenes(n):
	lista = range(2, n+1)
	lista_primo = [2]
	i = 1
	while i == 1:
		primo = lista[0]
		n = lista[-1] + 1
		lista.remove(primo)
		for n in lista:
			if n % primo == 0:
				lista.remove(n)
		if len(lista) > 0:
			lista_primo.append(lista[0])
			i = 1
		else:
			return lista_primo
			i = 0
		
print CrivoDeEratostenes(80)
