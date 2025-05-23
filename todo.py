import os

# Arquivo onde as tarefas serão salvas
ARQUIVO = "tarefas.txt"

# Carrega as tarefas do arquivo
def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as arquivo:
        return [linha.strip() for linha in arquivo.readlines()]

# Salva as tarefas no arquivo
def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(tarefa + "\n")

# Mostra o menu
def mostrar_menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Remover tarefa")
    print("4 - Sair")

#  principal
def main():
    tarefas = carregar_tarefas()

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            if not tarefas:
                print("Nenhuma tarefa encontrada.")
            else:
                print("\nSuas tarefas:")
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa}")

        elif escolha == "2":
            nova = input("Digite a nova tarefa: ")
            tarefas.append(nova)
            salvar_tarefas(tarefas)
            print("Tarefa adicionada!")

        elif escolha == "3":
            if not tarefas:
                print("Nenhuma tarefa para remover.")
            else:
                print("\nEscolha a tarefa para remover:")
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa}")
                try:
                    num = int(input("Número da tarefa: "))
                    if 1 <= num <= len(tarefas):
                        removida = tarefas.pop(num - 1)
                        salvar_tarefas(tarefas)
                        print(f"Tarefa '{removida}' removida.")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Por favor, digite um número.")

        elif escolha == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
2