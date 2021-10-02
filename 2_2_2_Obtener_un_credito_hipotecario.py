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
    print("El monto puede ser aprobado")
else:
    validador=False
    print("El monto debe ser superior a $500.000.-")

if cuotas>=3 and cuotas <=84:
    print(f"La cantidad {cuotas} de cuotas son validas")
else:
    validador=False
    print("Debe ingresar un valor entre 3 y 84 cuotas")

