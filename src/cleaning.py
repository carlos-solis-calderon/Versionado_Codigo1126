def limpiar_texto(texto):
    return texto.strip().lower()

def quitar_duplicados(filas):
    return list(dict.fromkeys(filas))