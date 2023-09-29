def es_primo(numero):
    """Verifica si un número es primo."""
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        entrada_usuario = int(input("Ingresa un número entero: "))
        if es_primo(entrada_usuario):
            print(f"{entrada_usuario} es un número primo.")
        else:
            print(f"{entrada_usuario} no es un número primo.")
    except ValueError:
        print("Por favor, ingresa un entero válido.")

#----------------------------------------------------------------------------#
def es_primo(numero):
    """Verifica si un número es primo."""
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def siguiente_primo(n):
    """Encuentra y devuelve el primer número primo mayor que n."""
    candidato = n + 1
    while True:
        if es_primo(candidato):
            return candidato
        candidato += 1

if __name__ == "__main__":
    try:
        entrada_usuario = int(input("Ingresa un número entero: "))
        if entrada_usuario < 0:
            print("Por favor, ingresa un entero no negativo.")
        else:
            resultado = siguiente_primo(entrada_usuario)
            print(f"El siguiente número primo mayor que {entrada_usuario} es: {resultado}")
    except ValueError:
        print("Por favor, ingresa un entero válido.")
        
    
#------------------------------------------------------------------------------------------------------#

def mediana_de_tres(num1, num2, num3):
    """Devuelve el valor mediano de tres números."""
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros[1]

if __name__ == "__main__":
    try:
        # Obtener la entrada del usuario
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        num3 = float(input("Ingresa el tercer número: "))

        # Calcular y mostrar la mediana
        resultado = mediana_de_tres(num1, num2, num3)
        print(f"La mediana de {num1}, {num2} y {num3} es: {resultado}")
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

#------------------------------------------------------------------------------------------#

import random
import string

def generar_contraseña_aleatoria():
    """Genera una contraseña aleatoria con una longitud entre 7 y 10 caracteres."""
    longitud_contraseña = random.randint(7, 10)
    caracteres_contraseña = string.printable[33:127]  # Caracteres ASCII del 33 al 126

    # Generar contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres_contraseña) for _ in range(longitud_contraseña))
    return contraseña

if __name__ == "__main__":
    # Mostrar la contraseña generada aleatoriamente
    contraseña_aleatoria = generar_contraseña_aleatoria()
    print(f"Contraseña Aleatoria Generada: {contraseña_aleatoria}")

#-------------------------------------------------------------------------------------------------------------#

def calcular_hipotenusa(lado1, lado2):
    """Calcular la hipotenusa de un triángulo rectángulo utilizando el teorema de Pitágoras."""
    hipotenusa = (lado1**2 + lado2**2)**0.5
    return hipotenusa

if __name__ == "__main__":
    try:
        # Obtener la entrada del usuario
        lado1 = float(input("Ingresa la longitud del primer lado más corto: "))
        lado2 = float(input("Ingresa la longitud del segundo lado más corto: "))

        # Calcular y mostrar la hipotenusa
        resultado = calcular_hipotenusa(lado1, lado2)
        print(f"La longitud de la hipotenusa es: {resultado}")
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")
