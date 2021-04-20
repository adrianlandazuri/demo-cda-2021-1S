def signo(x):
    if x>0:
	resultado = 1
    else:
	if x == 0:
	    resultado = 0
	else:
	    resultado = -1
    return resultado

signo(10), signo(0) , signo(-10)
