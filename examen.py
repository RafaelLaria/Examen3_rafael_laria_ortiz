def filtrar_palabras(lista_palabras, letra):
    lista_final = []
    for i in lista_palabras:
        if i.startswith(letra):d
            lista_final.append(i)
    return lista_final
print(filtrar_palabras(["Hola", "adios", "Hielo"], "h"))