
anio = int (input("dame un año"))

if (anio %4 == 0 and anio % 100 !=0) or (anio %400 ==0):
    print(f"El año {anio}es bisiesto")
else:
    print(f"El ano{anio}no es bisiesto")