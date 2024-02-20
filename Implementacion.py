def adivinador(pensador, inicio, fin):
    if inicio <= fin:
        medio = (inicio + fin) // 2
        respuesta = pensador(medio)
        if respuesta == 0:
            return medio
        elif respuesta == 1:
            return adivinador(pensador, inicio, medio - 1)
        else:
            return adivinador(pensador, medio + 1, fin)
    else:
        return None

def pensador(numero_pensado):
    suposicion = int(input("¿Es " + str(numero_pensado) + "? (0: Igual, 1: Menor, 2: Mayor): "))
    return suposicion

def jugar_adivinar_numero():
    numero_pensado = int(input("Piense en un numero natural: "))
    intervalo_min = int(input("Ingrese el limite menor del intervalo: "))
    intervalo_max = int(input("Ingrese el limite mayor del intervalo: "))
    if intervalo_min >= intervalo_max:
        print("El limite menor del intervalo debe ser menor que el limite mayor")
        jugar_adivinar_numero()
    if numero_pensado < intervalo_min or numero_pensado>intervalo_max:
        print("El numero pensado debe estar dentro del intervalo")
        jugar_adivinar_numero()
    respuesta = adivinador(pensador, intervalo_min, intervalo_max)
    if respuesta is None:
        print("El adivinador no pudo encontrar el número.")
    else:
        print(f"El adivinador encontró el número {respuesta}.")

jugar_adivinar_numero()
