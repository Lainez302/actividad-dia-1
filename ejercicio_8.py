peso = float(input("cual es tu peso en (kg):"))
altura = float(input("cual es tu altura en metros (m):"))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"tu imc es {imc:.2f}. bajo peso.")
elif 18.5 <= imc < 25:
    print(f"tu imc es {imc:.2f}. normal.")
elif 25 <= imc < 30:
    print(f"tu imc es {imc: .2f}. sobrepeso.")    
else: 
    print(f"tu imc es {imc:.2f}. obesidad.")
