total_cuenta = float (input ("valor de la cuenta: $"))

print("¿quiere dejar una propina con el porcentaje de 10,15,20?")
print ("1. 10%")
print ("2. 15%")
print ("3. 20%")
porcentaje = int(input("selecciona 1, 2, 3: ") )

if porcentaje == 1:
    propina = total_cuenta * 0.10
elif porcentaje == 2:
    propina = total_cuenta * 0.15
elif porcentaje == 3:
    propina = total_cuenta * 0.20
else:
    print ("esta opcion no es valida.")
    propina = 0
    
print(f"la propina es: ${propina:.2f}")




