# OPERACIONES

# Las cuatro operaciones principales son: 
from math import ceil, floor


print(" ***** OPERACIONES EN PYTHON *****")
# Suma
print(" *** Suma *** ")
print(5+5)

# Resta
print(" *** Resta ***")
print(5-3)

# Multiplicación
print(" *** Multiplicación ***")
print(5*3)

# División
print(" *** División ***")
print(10/3)

# Redondear hacia abajo (division de piso)
print(" *** División de piso ***")
seconds = 1042
display_minutes = seconds // 60
print(display_minutes)


# Operador Módulo
print(" *** Módulo *** ")
display_seconds = seconds % 60
print(display_seconds)

# Convertir cadenas en números
# En python se admiten dos tipos principales de números: int y float
print(" *** Convirtiendo una cadena a un número entero: int() *** ")
demo_int = int('125')
print(demo_int)

print(" *** Convirtiendo una cadena a un número flotante: float() *** ")
demo_float = float('215.3')
print(demo_float)

# Valor Absoluto
print(" *** Sacando el valor absoluto de una resta en la que el resultado normal es negativo: abs() *** ")
print(abs(39-16))
print(abs(10-50))


# Redondeo
print(" *** Redondeando números: round() *** ")
print("Redondeando el número 18.5615")
print(round(18.5615))

# Redondeo hacia arriba y hacia abajo: ceil() , floor()
print("Redondeando el número 15.45 hacia arriba")
print(ceil(15.45))
print("Redondeando el número 15.45 hacia abajo")
print(floor(15.45))
