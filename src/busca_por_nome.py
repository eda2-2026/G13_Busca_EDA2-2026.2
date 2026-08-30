from tabela_hash import TabelaHash
from src.normaliza import normalizar

def construir_indice_nome(disciplinas):
    indice = TabelaHash(capacidade_inicial=max(16, len(disciplinas) * 4))
    for d in disciplinas:
        for palavra in normalizar(d["nome"]).split():
            existentes = indice.buscar(palavra)
            if existentes is None:
                indice.inserir(palavra, [d])
            else:
                existentes.append(d)
    return indice

def busca_por_nome(indice, termo):
    resultado = indice.buscar(normalizar(termo))
    return resultado if resultado else []
