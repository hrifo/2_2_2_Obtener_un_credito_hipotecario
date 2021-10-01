nombre_cliente=input("Ingrese el nombre del cliente: ")
rut_cliente=input("Ingrese el rut del cliente: ")
nacionalidad=input("Ingrese nacionalidad: ")
sueldo=int(input("Ingrese su sueldo: "))
antiguedad=int(input("Ingrese su antigüedad laboral (en años): "))
morosidades=input("¿Tiene morosidades?: ")


valido1 = 0
while valido1 == 0:
    monto_credito=int(input("Ingrese el monto a solicitar: "))
    if monto_credito>=500000:
        print("El monto está en el rango solicitado.")
        valido = 1
    else:
        print("Debe solicitar un monto sobre $500.000")

valido2 = 0
while valido2 == 0:
    cuotas_credito=int(input("Ingrese el plazo de cuotas: "))
    if cuotas_credito>=3 and cuotas_credito<=84:
        print("Las cuotas están en el rango solicitado.")
        valido = 1
    else:
        print("Las cuotas están fuera del rango")

valido3 = 0
while valido3 == 0:
    edad_cliente=int(input("Ingrese su edad: "))
    if edad_cliente>=24 and edad_cliente<=79:
        print("El rango de edad es correcto.")
        valido = 1
    else:
        print("Se encuentra fuera de la edad solicitada")
