def filtrar_palabras(lista_palabras, letra):
    lista_final = []
    letra = letra.lower()
    for i in lista_palabras:
        if i.lower()startswith(letra):
            lista_final.append(i)
    return lista_final.sorted()
print(filtrar_palabras(["Hola", "adios", "Hielo"], "h"))