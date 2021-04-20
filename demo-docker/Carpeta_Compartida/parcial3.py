print("**********************************************************************")
print("Bienvenido a su programa de cálculo de funciones trigonométricas")
print("***********************************************************************")

def seno(x,z):
    sen = int(z)/int(x)
    return sen
def coseno(x, y):
    cosen = int(y)/int(x)
    return cosen
def tangente(z, y):
    tangen = int(z)/int(y)
    return tangen
def cosecante(x, z):
    cosecan = int(x)/int(z)
    return cosecan
def secante(x,y):
    secan = int(x)/int(y)
    return secan
def cotangente(z,y):
    cotangen = int(y)/int(z)
    return cotangen

print("Ingresar el valor del lado x") #Valor de la Hipotenusa
x = input()

print("Ingresar el valor del lado y") #Valor del Cateto Adyacente
y = input()

print("Ingresar el valor del lado z") #Valor del Cateto Opuesto
z = input()

print("El seno es igual a: " + str(seno(x, z)))
print("El coseno es igual a: " + str(coseno(x, y)))
print("La tangente es igual a: " + str(tangente(z, y)))
print("La cosecante es igual a: " + str(cosecante(x, z)))
print("La secante es igual a: " + str(secante(x, y)))
print("La cotangente es igual a: " + str(cotangente(z, y)))
