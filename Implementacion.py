def adivinador(k, b, e):
    if b <= e:
        q = (b + e) // 2
        response = getGuessResponse(q)
        if response == 0:
            return q
        elif response == 1:
            return adivinador(k, b, q - 1)
        else:
            return adivinador(k, q + 1, e)
    else:
        return None

def getGuessResponse(pivote):
    response = int(input("¿Es " + str(pivote) + "? (0: Igual, 1: Menor, 2: Mayor): "))
    return response

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
    respuesta = adivinador(numero_pensado, intervalo_min, intervalo_max)
    if respuesta is None:
        print("El adivinador no pudo encontrar el número.")
    else:
        print(f"El adivinador encontró el número {respuesta}.")

jugar_adivinar_numero()
