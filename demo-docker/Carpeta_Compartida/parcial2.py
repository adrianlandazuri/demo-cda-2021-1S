
print("**********************************************************************")
print("Bienvenido a su programa de cálculo de funciones trigonométricas")
print("***********************************************************************")

def seno(x,y):
    sen = int(y)/int(x)
    return sen
def coseno(x, z):
    cosen = int(z)/int(x)
    return cosen
def tangente(y,z):
    tangen = int(y)/int(z)
    return tangen
def cosecante(x, y):
    cosecan = int(x)/int(y)
    return cosecan
def secante(x, z):
    secan = int(x)/int(z)
    return secan
def cotangente(y,z):
    cotangen = int(z)/int(y)
    return cotangen

print("Ingresar el valor del lado x") #Valor de la Hipotenusa
x = input()

print("Ingresar el valor del lado y") #Valor del Cateto Opuesto
y = input()

print("Ingresar el valor del lado z") #Valor del Cateto Adyacente
z = input()

print("El seno es igual a: " + str(seno(x, y)))
print("El coseno es igual a: " + str(coseno(x, z)))
print("La tangente es igual a: " + str(tangente(y, z)))
print("La cosecante es igual a: " + str(cosecante(x, y)))
print("La secante es igual a: " + str(secante(x, z)))
print("La cotangente es igual a: " + str(cotangente(y, z)))
