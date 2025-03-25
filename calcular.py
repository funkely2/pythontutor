def calcular():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            operador = input("Ingrese la operación (+, -, *, /) o 'q' para salir: ")
            if operador.lower() == 'q':
                print("Saliendo de la calculadora...")
                break
            num2 = float(input("Ingrese el segundo número: "))
            
            if operador == '+':
                resultado = num1 + num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
            elif operador == '/':
                if num2 == 0:
                    print("Error: No se puede dividir por cero.")
                    continue
                resultado = num1 / num2
            else:
                print("Operador no válido. Inténtelo de nuevo.")
                continue
            
            print(f"El resultado es: {resultado}")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese números válidos.")

if __name__ == "__main__":
    calcular()
