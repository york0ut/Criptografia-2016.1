import time
def resto(a,b):
	R=a
	while R >= b:
		R= R-b
	return(R)
	
comeco = time.time()
resto(12345678, 2)
#print 12345678 % 2
fim = time.time()
print(fim - comeco)
