from src.carregaDados import carregar_disciplinas
from src.busca_binaria import busca_binaria
from src.busca_por_nome import construir_indice_nome, busca_por_nome
from src.busca_por_professor import construir_indice_professor, busca_por_professor


def imprimir_resultados(resultados):
    if resultados:
        for r in resultados:
            print(f"{r['codigo']} - {r['nome']} ({r['professor']})")
    else:
        print("Nenhuma disciplina encontrada.")


def main():
    disciplinas = carregar_disciplinas()
    indice_nome = construir_indice_nome(disciplinas)
    indice_professor = construir_indice_professor(disciplinas)

    while True:
        print("1 - Buscar por codigo (busca binaria)")
        print("2 - Buscar por nome (tabela hash)")
        print("3 - Buscar por professor (tabela hash)")
        print("0 - Sair")
        opcao = input("Opcao: ").strip()

        if opcao == "1":
            codigo = input("Codigo: ").strip().upper()
            r = busca_binaria(disciplinas, codigo)
            imprimir_resultados([r] if r else [])
        elif opcao == "2":
            termo = input("Palavra do nome: ").strip()
            imprimir_resultados(busca_por_nome(indice_nome, termo))
        elif opcao == "3":
            professor = input("Nome do professor: ").strip()
            imprimir_resultados(busca_por_professor(indice_professor, professor))
        elif opcao == "0":
            break
        else:
            print("Opcaoo invalida.")


main()