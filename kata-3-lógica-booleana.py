# EJERCICIO 1 - Escribir declaraciones if, else y elif

# Variable que donde se guarda la velocidad del asteroide

# Solucion realizada

velocity = 49

if velocity > 25:
    print("¡ALERTA! un asteroide se acerca a la Tierra demasiado rápido")
    if velocity >= 19:
        print("El asteroide acercandose a la Tierra a una velocidad de " + str(velocity) + "km/s ,busque el rayo de luz que este esta produciendo")
elif velocity >= 19:
    print("Hay un asteroide acercandose a la Tierra a una velocidad de " + str(velocity) + " ,busque el rayo de luz que este esta produciendo")
else: 
    print("Siga tranquilo, no se encuentra ningún asteroide acercandose a la tierra demasiado rápido")    


# Problema 1

velocity = 49
if velocity > 25:
    print("¡ALERTA! un asteroide se acerca a la Tierra demasiado rápido")
else:
    print("Siga tranquilo, no se encuentra ningún asteroide acercandose a la tierra demasiado rápido")   


# Problema 2
velocity = 19
if velocity > 20:
    print("Hay un asteroide acercandose a la Tierra a una velocidad de " + str(velocity) + " ,busque el rayo de luz que este esta produciendo")
elif velocity == 20:
    print("Hay un asteroide acercandose a la Tierra a una velocidad de " + str(velocity) + " ,busque el rayo de luz que este esta produciendo")
else:
    print("Siga tranquilo, no se encuentra ningún asteroide acercandose a la tierra demasiado rápido") 


# EJERCICIO 2: Uso de operadores and y or

# Variables donde se guarda la velocidad y el tamano del asteroide

# Problema 3
velocity = 25
size = 40

if velocity > 25 and size > 25:
    print("¡ALERTA! Un asteroide muy peligroso se esta acercando a la Tierra")
elif velocity >= 20:
    print("Hay un asteroide acercandose a la Tierra a una velocidad de " + str(velocity) + " ,busque el rayo de luz que este esta produciendo")
elif size < 25:
    print("No hay nada de que preocuparse, sigue tranquilo")
else:
    print("No hay nada de que preocuparse, sigue tranquilo")