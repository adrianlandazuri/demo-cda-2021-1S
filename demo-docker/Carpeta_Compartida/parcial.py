
print("***************************************************")
print("Bienvenido a su programa de cálculo de pendiente")
print("***************************************************")

def calcularpendiente(x1, y1, x2, y2):
    pendiente = (int(y2) - int(y1))/(int(x2) - int(x1))
    return "El valor de la pendiente es: " + str(pendiente)

print("Por favor ingresar el valor para X1")
x1 = input()
print("Por favor ingresar el valor para Y1")
y1 = input()
print("Por favor ingresar el valor para X2")
x2 = input()
print("Por favor ingresar el valor para Y2")
y2 = input()

print(calcularpendiente(x1, y1, x2, y2))