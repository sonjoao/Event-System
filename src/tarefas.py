from src.arquivos import ler_arquivo, salvar_arquivo, adicionar_linha
from src.eventos import buscar_evento_por_id, listar_eventos

ARQUIVO_TAREFAS = "dados/tarefas.txt"


def gerar_id_tarefa():
    
    tarefas = ler_arquivo(ARQUIVO_TAREFAS)

    if len(tarefas) == 0:
        return 1

    ultima_tarefa = tarefas[-1]
    ultimo_id = int(ultima_tarefa.split(";")[0])

    return ultimo_id + 1


def criar_tarefa():
    print("\n=== Cadastro de Tarefa ===")

    listar_eventos()

    id_evento = input("\nDigite o ID do evento dessa tarefa: ")

    if buscar_evento_por_id(id_evento) is None:
        print("Evento não encontrado. Cadastre um evento válido primeiro.")
        return

    id_tarefa = gerar_id_tarefa()
    nome_tarefa = input("Nome da tarefa: ")

    while True:
        try:
            custo = float(input("Custo da tarefa: R$ "))
            break
        except ValueError:
            print("Digite apenas números no custo.")

    status = "pendente"

    linha = f"{id_tarefa};{id_evento};{nome_tarefa};{custo};{status}"
    adicionar_linha(ARQUIVO_TAREFAS, linha)

    print("\nTarefa cadastrada com sucesso!")


def listar_tarefas():
    print("\n=== Lista de Tarefas ===")

    tarefas = ler_arquivo(ARQUIVO_TAREFAS)

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada ainda.")
        return

    for tarefa in tarefas:
        dados = tarefa.split(";")

        print("-" * 40)
        print(f"ID da tarefa: {dados[0]}")
        print(f"ID do evento: {dados[1]}")
        print(f"Tarefa: {dados[2]}")
        print(f"Custo: R$ {float(dados[3]):.2f}")
        print(f"Status: {dados[4]}")


def listar_tarefas_por_evento(id_evento):
    
    tarefas = ler_arquivo(ARQUIVO_TAREFAS)
    encontrou = False

    print("\n=== Tarefas do Evento ===")

    for tarefa in tarefas:
        dados = tarefa.split(";")

        if dados[1] == str(id_evento):
            encontrou = True
            print("-" * 40)
            print(f"ID da tarefa: {dados[0]}")
            print(f"Tarefa: {dados[2]}")
            print(f"Custo: R$ {float(dados[3]):.2f}")
            print(f"Status: {dados[4]}")

    if not encontrou:
        print("Esse evento ainda não possui tarefas.")


def concluir_tarefa():
    print("\n=== Concluir Tarefa ===")

    listar_tarefas()

    id_concluir = input("\nDigite o ID da tarefa concluída: ")

    tarefas = ler_arquivo(ARQUIVO_TAREFAS)
    novas_tarefas = []
    encontrado = False

    for tarefa in tarefas:
        dados = tarefa.split(";")

        if dados[0] == id_concluir:
            encontrado = True
           
            tarefa_atualizada = f"{dados[0]};{dados[1]};{dados[2]};{dados[3]};concluida"
            novas_tarefas.append(tarefa_atualizada)
        else:
            novas_tarefas.append(tarefa)

    salvar_arquivo(ARQUIVO_TAREFAS, novas_tarefas)

    if encontrado:
        print("\nTarefa marcada como concluída!")
    else:
        print("\nTarefa não encontrada.")


def excluir_tarefa():
    print("\n=== Excluir Tarefa ===")

    listar_tarefas()

    id_excluir = input("\nDigite o ID da tarefa que deseja excluir: ")

    tarefas = ler_arquivo(ARQUIVO_TAREFAS)
    novas_tarefas = []
    encontrado = False

    for tarefa in tarefas:
        dados = tarefa.split(";")

        if dados[0] == id_excluir:
            encontrado = True
        else:
            novas_tarefas.append(tarefa)

    salvar_arquivo(ARQUIVO_TAREFAS, novas_tarefas)

    if encontrado:
        print("\nTarefa excluída com sucesso!")
    else:
        print("\nTarefa não encontrada.")
