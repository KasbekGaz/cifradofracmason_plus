# * definicion de variables
cuadricula1 = [
    ['j', 'B', 'C'],
    ['D', 'L', 'R'],
    ['G', 'H', 'P']
]
cuadricula2 = [
    ['A', 'K', 'E'],
    ['M', 'U', 'F'],
    ['I', 'Q', 'O']
]
cruz1 = [
    ['T', 'S'],
    ['V', 'N']
]
cruz2 = [
    ['x', 'W'],
    ['Z', 'Y']
]
secciones = [cuadricula1, cuadricula2, cruz1, cruz2]

# * FUNCION PARA ROTAR A LA IZQUIERDA


def rotar_izquierda(seccion, num_rotaciones):
    filas = len(seccion)
    columnas = len(seccion[0])
    for _ in range(num_rotaciones):
        nueva_seccion = [[None] * columnas for _ in range(filas)]
        for i in range(filas):
            for j in range(columnas):
                if seccion[i][j] is not None:
                    nueva_seccion[i][(j - 1 + columnas) %
                                     columnas] = seccion[i][j]
        seccion = nueva_seccion
    return seccion

# * Función para intercambiar la letra en la esquina superior derecha con la del centro


def intercambiar_esquina_centro(seccion):
    filas = len(seccion)
    columnas = len(seccion[0])
    if filas == 3 and columnas == 3:
        temp = seccion[0][2]
        seccion[0][2] = seccion[1][1]
        seccion[1][1] = temp
    return seccion


# Número de rotaciones para cada sección
num_rotaciones = [3, 3, 3, 3]  # 1 rotación para cada sección

# Aplicar rotaciones a las secciones
secciones_rotadas = [rotar_izquierda(
    seccion, num_rotaciones[i]) for i, seccion in enumerate(secciones)]

# Intercambiar las letras solo en las cuadrículas (no en las cruces)
secciones_intercambiadas = [intercambiar_esquina_centro(
    seccion) if i < 2 else seccion for i, seccion in enumerate(secciones_rotadas)]

# Función para crear el diccionario de cifrado


def crear_diccionario(secciones):
    diccionario = {}
    for seccion in secciones:
        for fila in seccion:
            for letra in fila:
                if letra is not None:
                    indice = fila.index(letra)
                    letra_rotada = fila[(indice + 1) % len(fila)] if fila[(indice + 1) %
                                                                          len(fila)] is not None else fila[(indice + 2) % len(fila)]
                    diccionario[letra] = letra_rotada
    return diccionario


diccionario_cifrado = crear_diccionario(secciones_intercambiadas)

# Función para cifrar un mensaje


def cifrar_mensaje(mensaje, diccionario):
    mensaje_cifrado = ''
    for letra in mensaje:
        if letra in diccionario:
            mensaje_cifrado += diccionario[letra]
        else:
            mensaje_cifrado += letra  # Dejar intactos los caracteres que no están en el diccionario
    return mensaje_cifrado


# Ejemplo de uso
mensaje = "HOLA SOY OSWALDO"
mensaje_cifrado = cifrar_mensaje(mensaje, diccionario_cifrado)
print("Mensaje a cifrar:", mensaje)
print("Mensaje cifrado:", mensaje_cifrado)
print("diccionario", diccionario_cifrado)
