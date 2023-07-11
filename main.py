#Ejercicio 1
def digitos(numero_de_tarjeta: str) -> int:
    return len(numero_de_tarjeta)

#Ejercicio 2
def obtener_prefijo(numero_de_tarjeta: str, tamaño_prefijo: int) -> int:
    prefijo = int(numero_de_tarjeta[:tamaño_prefijo])
    return prefijo

#Ejercicio 3
def tipo_tarjeta(numero_de_tarjeta: str) -> str:
    num_digitos = digitos(numero_de_tarjeta)
    prefijo = obtener_prefijo(numero_de_tarjeta, 2)  # Se obtienen los primeros 2 dígitos
    
    if num_digitos == 15 and (prefijo == 34 or prefijo == 37):
        return 'American Express'
    elif num_digitos == 16 and prefijo in range(51, 56):
        return 'Mastercard'
    elif num_digitos in [13, 16] and str(prefijo)[0] == '4':
        return 'Visa'
    else:
        return 'Invalid'

#Ejercicio 4
def digitos_impares(numero_de_tarjeta: str) -> list[int]:
    digitos = [int(numero_de_tarjeta[i]) for i in range(len(numero_de_tarjeta)-1, -1, -2)]
    return digitos

#Ejercicio 5
def digitos_pares(numero_de_tarjeta: str) -> list[int]:
    digitos = [int(numero_de_tarjeta[i]) for i in range(len(numero_de_tarjeta)-2, -1, -2)]
    return digitos

#Ejercicio 6
def sumar_digitos(lista_digitos: list[int]) -> int:
    suma = 0
    
    for numero in lista_digitos:
        numero_str = str(numero)  # Convertir el número a string
        for digito in numero_str:
            suma += int(digito)  # Sumar cada dígito a la suma total
    
    return suma

#Ejercicio 7
def luhn(numero_de_tarjeta :  str) -> bool:
    #1
    lista_pares = digitos_pares(numero_de_tarjeta)

    #2
    lista_pares_multiplicados = []

    for numero in lista_pares:
        lista_pares_multiplicados.append(str(numero * 2))

    #3
    suma_pares = 0

    for numero in lista_pares_multiplicados:
        for digito in numero:
            suma_pares += int(digito)

    #4
    lista_impares = digitos_impares(numero_de_tarjeta)

    #5
    suma_impares = 0

    for numero in lista_impares:
        suma_impares += numero

    suma_digitos = suma_impares + suma_pares

    #6
    return suma_digitos % 10 == 0

#Ejercicio 8
def validar_tarjeta(numero_de_tarjeta : str) -> bool:
    return tipo_tarjeta(numero_de_tarjeta) and luhn(numero_de_tarjeta)