from src.carregaDados import carregar_disciplinas
from src.busca_binaria import busca_binaria

def main():
    disciplinas = carregar_disciplinas()
    codigo = input("Código da disciplina: ").strip().upper()
    resultado = busca_binaria(disciplinas, codigo)
    if resultado:
        print(f"{resultado['codigo']} - {resultado['nome']} ({resultado['professor']})")
    else:
        print("Disciplina não encontrada.")

if __name__ == "__main__":
    main()
