nombre=input("Ingrese su nombre:")
run=input("Ingrese su run:")
monto=int(input("Ingrese monto a solicitar:"))
cuotas=int(input("Ingrese numero de cuotas:"))
edad=int(input("Ingrese su edad:"))
nacionalidad=input("Ingrese nacionalidad:")
sueldo=int(input("Ingrese su sueldo:"))
antiguedad=float(input("Ingrese antigüedad laboral: "))
morosidad=input("¿Tiene morosidades? (si/no)")

validador = True

if monto>500000:
    print("El monto puede ser aprobado\n")
else:
    validador=False
    print("El monto debe ser superior a $500.000.-\n")

if cuotas>=3 and cuotas <=84:
    print(f"La cantidad {cuotas} de cuotas son validas\n")
else:
    validador=False
    print("Debe ingresar un valor entre 3 y 84 cuotas\n")

if edad>=24 and edad<=79:
    print(f"La edad {edad} es valida\n")
else:
    validador=False
    print("No cumple con requisitos de edad\n")

if nacionalidad == "chilena":
    print("Cumple con requisitos de nacionalidad\n")
else:
    validador=False
    print("No cumple los requisitos de nacionalidad\n")

sueldo_monto = sueldo*10

if sueldo>=300000 and sueldo_monto>=monto:
    print("Cumple con los requisitos de sueldo\n")
else:
    validador=False
    print("No cumple con requisitos de sueldo\n")

if antiguedad>=3:
    print("Cumple requisitos de antigüedad laboral\n")
else:
    validador=False
    print("No cumple requitos de antiguedad laboral\n")

if morosidad == "no":
    print("Cumple con requisitos, no registra morosidad\n")
else:
    validador=False
    print("No cumple, registra morosidades\n")

if validador == True:
    monto_maximo=sueldo*10
    print("--------------------------------------------------------")
    print(f"{nombre}\t{run}")
    print("--------------------------------------------------------")
    print("Cumple con los requisitos")
    print(f"Sueldo: {sueldo}")
    print("Monto máximo: ",monto_maximo)
    print("Monto solicitado: ",monto)
    print("Taza mensual: 1,46%")
    print("Cuotas: ",cuotas)
    print("Monto a pagar: ",monto*1.46)
    print("--------------------------------------------------------")

else:
    print("--------------------------------------------------------")
    print(f"{nombre}\t{run}")
    print("--------------------------------------------------------")
    print("No cumple con los requisitos")
    print("--------------------------------------------------------")
    
