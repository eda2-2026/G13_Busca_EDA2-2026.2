def insertion_sort(disciplinas):
    
    lista = list(disciplinas)

    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        while j >= 0 and lista[j]["codigo"] > atual["codigo"]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = atual

    return lista
