def busca_binaria(disciplinas, codigo_alvo):
    lista = sorted(disciplinas, key=lambda d: d["codigo"])
    lo, hi = 0, len(lista) - 1
    while lo <= hi:
        meio = (lo + hi) // 2
        atual = lista[meio]["codigo"]
        if atual == codigo_alvo:
            return lista[meio] 
        if atual < codigo_alvo:
            lo = meio + 1
        else:
            hi = meio - 1
    return None
