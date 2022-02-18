# KATA 9 -FUNCIONES

# Función para los 3 tanques de combustible
def generar_reporte(tanque1, tanque2, tanque3):
    # Calculando el promedio
    promedio = promedio_tanque(tanque1, tanque2, tanque3)
    #Imprimiendo el 
    print(f"""Reporte de los tanques del cohete
    Promedio de los tanques = {promedio}
    Tanque 1: {tanque1} % 
    Tanque 2: {tanque2} %
    Tanque 3: {tanque3} %""" )


# Función para calcular el promedio de los tanques
def promedio_tanque(t1,t2,t3):
    return (t1 + t2 + t3) /3


generar_reporte(5,6,7)

# EJERCICIO 2
def reporte_mision(destino, *minutos, **tanques):
    principal_reporte = f"""
    Mission to {destino}
    Total travel time: {sum(minutos)} minutes
    Total fuel left: {sum(tanques.values())}
    """
    for nombre_tanque, galones in tanques.items():
        principal_reporte += f"{nombre_tanque} tank --> {galones} gallons left\n"
    return principal_reporte

print(reporte_mision("Moon", 8, 11, 55, principal=300000, externa=20000))